from os import getenv
import bottle
from app import create_app

app = create_app()


if __name__ == '__main__':
    bottle.run(
        server=getenv('SERVER', default='wsgiref'),
        host=getenv('HOST', '127.0.0.1'),
        port=getenv('PORT', 8080),
        reloader=getenv('DEBUG', 1)
    )
