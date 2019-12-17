import json
from flask import request
from src.services import collection_service as service
from src.util.Util import object_dict
from src.model.Collection import Collection

def get_collections():
    json_return = json.dumps(service.get_all(), default=object_dict)
    return json_return

def insert_collection():
    try:
        collection = Collection(
            0,
            request.json['name'],
        )
        return service.insert(collection)
    except KeyError as e:
        return 'json invalido'
