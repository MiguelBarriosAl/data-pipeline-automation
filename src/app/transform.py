
def vehicule(event: dict):
    event_type = event['event']
    on = event['on']
    at = event['at']
    data = event['data']
    print(event_type)
    print(at)
    print(on)
    print(data)

def operating(event: dict):
    event_type = event['event']
    on = event['on']
    at = event['at']
    data = event['data']
    # carga de data a mysql tabla vihucule
    print(event_type)
    print(at)
    print(on)
    print(data)

data = [['2019-06-01-15-28-11-events.json', {'event': 'create', 'on': 'vehicle', 'at': '2019-06-01T18:28:11.894Z', 'data': {'id': 'd57e9c3e-3479-47cd-9b20-9e317616a3f0', 'location': {'lat': 52.44173, 'lng': 13.42464, 'at': '2019-06-01T18:28:11.894Z'}}, 'organization_id': 'org-id'}, {'event': 'update', 'on': 'vehicle', 'at': '2019-06-01T18:28:11.894Z', 'data': {'id': 'd38656b3-1e9b-447f-a029-148603b6fc41', 'location': {'lat': 52.52894, 'lng': 13.2378, 'at': '2019-06-01T18:28:11.894Z'}}, 'organization_id': 'org-id'}, {'event': 'update', 'on': 'vehicle', 'at': '2019-06-01T18:28:11.894Z', 'data': {'id': 'cf25c1c6-1889-4dd1-95df-18141c4c746c', 'location': {'lat': 52.45875, 'lng': 13.28348, 'at': '2019-06-01T18:28:11.894Z'}}, 'organization_id': 'org-id'}], ['2019-06-01-15-28-12-events.json', {'event': 'update', 'on': 'vehicle', 'at': '2019-06-01T18:28:12.904Z', 'data': {'id': 'd57e9c3e-3479-47cd-9b20-9e317616a3f0', 'location': {'lat': 52.4417, 'lng': 13.42453, 'at': '2019-06-01T18:28:12.904Z'}}, 'organization_id': 'org-id'}, {'event': 'update', 'on': 'vehicle', 'at': '2019-06-01T18:28:12.905Z', 'data': {'id': 'd38656b3-1e9b-447f-a029-148603b6fc41', 'location': {'lat': 52.52904, 'lng': 13.23706, 'at': '2019-06-01T18:28:12.905Z'}}, 'organization_id': 'org-id'}, {'event': 'update', 'on': 'vehicle', 'at': '2019-06-01T18:28:12.905Z', 'data': {'id': 'cf25c1c6-1889-4dd1-95df-18141c4c746c', 'location': {'lat': 52.45877, 'lng': 13.28334, 'at': '2019-06-01T18:28:12.905Z'}}, 'organization_id': 'org-id'}]]


[vehicule(inner_dict) if inner_dict['event'] in ('create', 'delete') else operating(inner_dict) for inner_list in data for inner_dict in
       inner_list[1:]]






