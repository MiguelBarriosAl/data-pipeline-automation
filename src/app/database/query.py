
def insert_events(id_event, file, event, on_event, at_event, organization_id):
    return """INSERT INTO events (id_event, file, event, on_event , at_event, organization_id) VALUES (%s, %s, %s, %s, %s, %s);""" % \
           (id_event, file, event, on_event, at_event, organization_id)


def insert_vehicles(id_event, id_vehicle, lat, lng, at_vehicle):
    return """INSERT INTO vehicles (id, id_vehicle, lat , lng, at_vehicle) VALUES (%s, %s, %s, %s, %s);""" % \
           (id_event, id_vehicle, lat, lng, at_vehicle)


def insert_operating_period(id_event, id_vehicle, lat , lng, at_vehicle):
    return """INSERT INTO vehicles (id, id_vehicle, lat , lng, at_vehicle) VALUES (%s, %s, %s, %s, %s);""" % \
           (id_event, id_vehicle, lat, lng, at_vehicle)
