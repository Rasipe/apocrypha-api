import json
from flask import request
from src.services import publisher_service as service
from src.util.Util import object_dict
from src.model.Publisher import Publisher


def get_publishers():
    json_return = json.dumps(service.get_all(), default=object_dict)
    return json_return

def insert_publisher():
    try:
        publisher = Publisher(
            0,
            request.json['name'],
        )
        return service.insert(publisher)
    except KeyError as e:
        return 'json invalido'
