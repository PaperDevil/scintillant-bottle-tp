"""
    errors.py - HTTP Exception Handling Methods
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Basic description of exception handling within HTTP route handling functions
"""
from bottle import error
from bottle import response


@error(404)
def error_not_found(err):
    """
    The requested resource could not be found but may be available in the future.
    Subsequent requests by the client are permissible.

    :param err:
    :return:
    """

    return "Sorry, this route not found!"


@error()
def error_unexpected(err):
    """
    In case of unexpected errors, the request will be processed by this function.
    In this case, it is possible to generate a convenient response from the bot for a successful system shutdown.

    :param err:
    :return:
    """

    response.status = 500
    return f"Unexpected error inside server \n\n{err}"
