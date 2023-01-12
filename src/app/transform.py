import datetime
import os

from dotenv import load_dotenv
from src.app.checkers import check_fields
from src.app.database.connector import Database
from src.app.database.query import insert_events, insert_vehicles, insert_operating_period
from src.app.utils import generate_id
from src.constant import HOST, USER, PASSWORD, DB

HOST = os.getenv('DB_ADDRESS')
PASSWORD = os.getenv('DB_PASS')
DB = os.getenv('DB_DATABASE')
USER = os.getenv('DB_USER')


events_fields = ["event", "on", "at", "data", "organization_id"]
vehicles_fields = ["id", "location"]
vehicles_deregister_fields = ["id"]
operating_period_fields = ["id", "start", "finish"]


def transform_date(date_string):
    date_object = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_object.strftime("%Y-%m-%d %H:%M:%S")


def event_data(data: dict) -> list:
    check_fields(data, events_fields)
    event_type = data['event']
    on = data['on']
    at = transform_date(data['at'])
    organization_id = data['organization_id']
    return [event_type, on, at, organization_id]


def vehicle_data(data: dict) -> list:
    check_fields(data, vehicles_fields)
    id_vehicle = data['id']
    lat = data['location']['lat']
    lng = data['location']['lng']
    at_vehicle = transform_date(data['location']['at'])
    return [id_vehicle, lat, lng, at_vehicle]


def vehicle_deregister_data(data: dict) -> list:
    print(data)
    check_fields(data, vehicles_deregister_fields)
    id_vehicle = data['id']
    lat = None
    lng = None
    at_vehicle = None
    return [id_vehicle, lat, lng, at_vehicle]

def operating_period_data(data: dict) -> list:
    check_fields(data, operating_period_fields)
    id_operating = data['id']
    start = transform_date(data['start'])
    finish = transform_date(data['finish'])
    return [id_operating, start, finish]


def transform_n_load(data: list):
    db = Database(host='localhost',
                  database='door2door',
                  user='root',
                  password='password')
    for inner_list in data:
        file = inner_list[0]
        for inner_dict in inner_list[1:]:
            id_event = generate_id()
            event = event_data(inner_dict)
            query_insert_event = insert_events(id_event, file, event[0], event[1], event[2], event[3])
            db.query(query_insert_event)
            if inner_dict['event'] in ('register', 'update'):
                vehicle = vehicle_data(inner_dict['data'])
                query_insert_vehicle = insert_vehicles(id_event, vehicle[0], vehicle[1], vehicle[2], vehicle[3])
                db.query(query_insert_vehicle)

            elif inner_dict['event'] in 'deregister':
                vehicle = vehicle_deregister_data(inner_dict['data'])
                query_insert_vehicle = insert_vehicles(id_event, vehicle[0], vehicle[1], vehicle[2], vehicle[3])
                db.query(query_insert_vehicle)

            elif inner_dict['event'] in ('create', 'delete'):
                operating = operating_period_data(inner_dict['data'])
                query_operating_period = insert_operating_period(id_event, operating[0], operating[1], operating[2])
                db.query(query_operating_period)








