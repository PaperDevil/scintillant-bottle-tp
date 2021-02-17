from bottle import get
import json
import os


@get('/snlt')
def snlt_settings():
    with open(os.getcwd() + '/.snlt') as snlt:
        data = json.load(snlt)
    return data
