"""
    options.py - Configuring CORS and headers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from os import getenv
from bottle import hook, route, response

_allow_origin = getenv('ALLOW_ORIGIN', '*')
_allow_methods = getenv('ALLOW_METHODS', 'GET, POST, PATCH, DELETE')
_allow_headers = getenv('ALLOW_HEADERS', '*')


@hook('after_request')
def enable_cors():
    """Add headers to enable CORS"""

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers


@route('/', method='OPTIONS')
def options_handler(path=None):
    """Returns basic application settings to the request client"""
    return
