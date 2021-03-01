import os

import requests
from scintillant.apimodels import SkillRequest


def send_data_to_skill(user, context, update):
    return requests.post('http://localhost:' + os.getenv('PORT') + '/skill', json=SkillRequest(
        user=SkillRequest.User(
            user_id=user.get('user_id'),
            client_app=user.get('client_app'),
            global_id=user.get('global_id')
        ),
        context=context,
        update=SkillRequest.Update(
            in_text=update.get('in_text', None),
            in_choice=update.get('in_choice', None),
            datetime=0
        )
    ).serialize_json())


def get_choice_from_name(choices: list, name: str):
    for choice in choices:
        if choice[0] == name:
            return choice
    return None
