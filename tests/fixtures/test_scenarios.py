from pytest_bdd import scenario, when, parsers
from utils import send_data_to_skill, get_choice_from_name
from data import *
from steps import *


@scenario(
    '../features/jkh.feature',
    'Успешная подача показаний больше предыдущих')
def test_counter_household_flat_manual_account():
    pass


@when(parsers.parse('Я пишу навыку: {text}'))
def send_to_skill(user, context, text):
    print(text)

    r = send_data_to_skill(user, context, {'in_text': text})
    assert r.status_code == 200

    context = r.json().get('context')
    context['__choices'] = r.json().get('choices')
    context['__out_text'] = r.json().get('out_text')


@when(parsers.parse('Я выбираю счётчик с номером {number}'))
def choose_counter(user, context, number: int):
    print(context)
    counter = context['__choices'][int(number)]
    assert counter

    r = send_data_to_skill(user, context, {'in_choice': counter[0]})
    assert r.status_code == 200

    context = r.json().get('context')
    context['__choices'] = r.json().get('choices')
    context['__out_text'] = r.json().get('out_text')


@when(parsers.parse('Я выбираю кнопку: {choice}'))
def choose_button(user, context, choice):
    print(choice)
    button = get_choice_from_name(context['__choices'], choice)

    r = send_data_to_skill(user, context, {'in_choice': button[1]})
    assert r.status_code == 200

    context = r.json().get('context')
    context['__choices'] = r.json().get('choices')
    context['__out_text'] = r.json().get('out_text')
