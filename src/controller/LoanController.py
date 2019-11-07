import json
from flask import request
from src.services import loan_service as service
from src.util.Util import object_dict
from src.model.Loan import Loan


def insert_loan():
    try:
        return service.insert(request.json)
    except KeyError as e:
        return 'json invalido'


def devolution(loan_id):
    try:
        return service.update(loan_id)
    except KeyError as e:
        return 'json invalido'
