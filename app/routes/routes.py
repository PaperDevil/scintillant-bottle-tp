"""
    routes.py - The main routes required by the Dialogue service.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    It is better not to modify this file so as not to cause errors
    in interaction with the Dialogs service.
    If you need to create new routes, you need to create a separate
    module and register it in the __init__.py of this application.
"""
from bottle import get, post
from bottle import request, response
from scintillant.apimodels import SkillRequest

from http import HTTPStatus

from app.skill_manager import States
from app.drivers.picklecache import PickleDBCache


@post('/skill')
def skill():
    data = SkillRequest(**request.json)
    user_context = PickleDBCache.get_or_create(f'{data.message.user.idx}_context')
    data.context = user_context
    answer = States(data=data).get_response()
    PickleDBCache.update(f'{data.message.user.idx}_context', answer.context)
    return answer.json()


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
