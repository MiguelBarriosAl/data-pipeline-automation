import datetime
from app.checkers import check_fields
from app.database.connector import Database
from app.database.query import insert_events, insert_vehicles, insert_operating_period, insert_vehicle_event
from app.utils import generate_id
from constant import HOST, USER, PASSWORD, DB, EVENT, VEHICLES, VEHICLES_DEREGISTER, OPERATING

"""
    Transform_n_load function takes a list of data as its parameter 
    and performs transformations on that data before loading 
    it into a specific database. It uses the helper functions 
    event_data, vehicle_update, vehicle_event, operating_period_data, 
    and transform_date to extract and transform the relevant information 
    before executing SQL queries to insert the data into  the database.
    It also uses a check_fields function to validate the fields of the json data.
    It uses a db connection object 'Database' to connect and run the queries on the database.
    It also uses 'generate_id' function to generate unique ids for the events.
    It uses insert_events, insert_vehicles, insert_vehicle_event, 
    insert_operating_period functions to generate the insert statements.
"""


def transform_date(date: str) -> str:
    date_object = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_object.strftime("%Y-%m-%d %H:%M:%S")


def event_data(data: dict) -> list:
    check_fields(data, EVENT)
    event_type = data['event']
    on = data['on']
    at = transform_date(data['at'])
    organization_id = data['organization_id']
    return [event_type, on, at, organization_id]


def vehicle_update(data: dict) -> list:
    check_fields(data, VEHICLES)
    id_vehicle = data['id']
    lat = data['location']['lat']
    lng = data['location']['lng']
    at_vehicle = transform_date(data['location']['at'])
    return [id_vehicle, lat, lng, at_vehicle]


def vehicle_event(data: dict) -> list:
    check_fields(data, VEHICLES_DEREGISTER)
    id_vehicle = data['id']
    lat = 'NULL'
    lng = 'NULL'
    at_vehicle = 'NULL'
    return [id_vehicle, lat, lng, at_vehicle]


def operating_period_data(data: dict) -> list:
    check_fields(data, OPERATING)
    id_operating = data['id']
    start = transform_date(data['start'])
    finish = transform_date(data['finish'])
    return [id_operating, start, finish]


def transform_n_load(data: list):
    """
    The function takes a list of data and performs transformations and loadings into a specified database.

    Parameters:
        data (list): List of data to be transformed and loaded into the database

    Returns:
        None
    """
    db = Database(host=HOST, database=DB, user=USER, password=PASSWORD)
    for inner_list in data:
        file = inner_list[0]
        for inner_dict in inner_list[1:]:
            id_event = generate_id()
            event = event_data(inner_dict)
            query_insert_event = insert_events(id_event, file, event[0], event[1], event[2], event[3])
            db.query(query_insert_event)
            if inner_dict['event'] in 'update':
                vehicle = vehicle_update(inner_dict['data'])
                query_insert_vehicle = insert_vehicles(id_event, vehicle[0], vehicle[1], vehicle[2], vehicle[3])
                db.query(query_insert_vehicle)
            elif inner_dict['event'] in ('deregister', 'register'):
                vehicle = vehicle_event(inner_dict['data'])
                query_insert_vehicle = insert_vehicle_event(id_event, vehicle[0], vehicle[1], vehicle[2], vehicle[3])
                db.query(query_insert_vehicle)
            elif inner_dict['event'] in ('create', 'delete'):
                operating = operating_period_data(inner_dict['data'])
                query_operating_period = insert_operating_period(id_event, operating[0], operating[1], operating[2])
                db.query(query_operating_period)
            else:
                print(f"Error data: {inner_dict}")








