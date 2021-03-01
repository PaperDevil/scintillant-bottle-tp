from pytest_bdd import given, then
import requests
import os
from scintillant.apimodels import SkillRequest
from utils import send_data_to_skill


@given("Начинаю общение с навыком")
def skill_initial_state(user, context):
    """ TODO Слать запрос с тектом 'Привет' """
    r = send_data_to_skill(user, context, {'in_text': 'Привет'})
    assert r.status_code == 200
    context = r.json().get('context')
    context['__choices'] = r.json().get('choices')
    context['__out_text'] = r.json().get('out_text')


@then("Заканчиваю общение с навыком")
def exit_of_skill(user, context):
    """ TODO Слать запрос с тектом 'exit' """
    r = send_data_to_skill(user, context, {'in_text': 'exit'})
    assert r.status_code == 200
    context = r.json().get('context')
    context['__choices'] = r.json().get('choices')
    context['__out_text'] = r.json().get('out_text')
