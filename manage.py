import os
from app import create_app

app = create_app()


def run_app(port='8080'):
    app.run(port=int(port))


if __name__ == '__main__':
    run_app(os.getenv('PORT'))
