from pytest_bdd import given, then, parsers, scenario, when
from utils import send_data_to_skill, get_choice_from_name
from data import user
import pytest

pytest.global_context = {}


@scenario(
    '../features/jkh.feature',
    'Успешная подача показаний больше предыдущих')
def test_counter_household_flat_manual_account():
    pass


@when(parsers.parse('Я пишу навыку: {text}'))
def send_to_skill(user, text):
    print(text)

    r = send_data_to_skill(user, pytest.global_context, {'in_text': text})
    assert r.status_code == 200

    pytest.global_context = r.json().get('context')
    pytest.global_context['__choices'] = r.json().get('choices')
    pytest.global_context['__out_text'] = r.json().get('out_text')


@when(parsers.parse('Я выбираю счётчик с номером {number}'))
def choose_counter(user, number: int):
    print(pytest.global_context)
    counter = pytest.global_context['__choices'][int(number)]
    assert counter

    r = send_data_to_skill(user, pytest.global_context, {'in_choice': counter[0]})
    assert r.status_code == 200

    pytest.global_context = r.json().get('context')
    pytest.global_context['__choices'] = r.json().get('choices')
    pytest.global_context['__out_text'] = r.json().get('out_text')


@when(parsers.parse('Я выбираю кнопку: {choice}'))
def choose_button(user, choice):
    print(choice)
    button = get_choice_from_name(pytest.global_context['__choices'], choice)

    r = send_data_to_skill(user, pytest.global_context, {'in_choice': button[1]})
    assert r.status_code == 200

    pytest.global_context = r.json().get('context')
    pytest.global_context['__choices'] = r.json().get('choices')
    pytest.global_context['__out_text'] = r.json().get('out_text')


@given("Начинаю общение с навыком")
def skill_initial_state(user):
    """ TODO Слать запрос с тектом 'Привет' """
    r = send_data_to_skill(user, pytest.global_context, {'in_text': 'Привет'})
    assert r.status_code == 200
    pytest.global_context = r.json().get('context')
    pytest.global_context.update({'__choices': r.json().get('choices')})
    pytest.global_context['__out_text'] = r.json().get('out_text')


@then("Заканчиваю общение с навыком")
def exit_of_skill(user):
    """ TODO Слать запрос с тектом 'exit' """
    r = send_data_to_skill(user, pytest.global_context, {'in_text': 'exit'})
    assert r.status_code == 200
    pytest.global_context = r.json().get('context')
    pytest.global_context['__choices'] = r.json().get('choices')
    pytest.global_context['__out_text'] = r.json().get('out_text')
