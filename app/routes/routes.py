"""
    routes.py - The main routes required by the Dialogue service.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    It is better not to modify this file so as not to cause errors
    in interaction with the Dialogs service.
    If you need to create new routes, you need to create a separate
    module and register it in the __init__.py of this application.
"""
from bottle import get, post, error
from bottle import request, response
from scintillant.apimodels import SkillRequest

from http import HTTPStatus

from app.skill_manager import States


@post('/skill')
def skill():
    manager = States(data=SkillRequest.from_dict(request.json))
    answer = manager.get_response()
    return answer.serialize_json()


@get('/logs')
def logs():
    ...


@get('/logs/all')
def logs_all():
    ...


@get('/')
@get('/health')
def health():
    """"""
    response.status = HTTPStatus.OK
