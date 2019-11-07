import json
from flask import request
from src.services import genre_service as service
from src.util.Util import object_dict
from src.model.Genre import Genre

def get_genres():
    json_return = json.dumps(service.get_all(), default=object_dict)
    return json_return

def insert_genre():
    try:
        genre = Genre(
            0,
            request.json['description'],
        )
        return service.insert(genre)
    except KeyError as e:
        return 'json invalido'
