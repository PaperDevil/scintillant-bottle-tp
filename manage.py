from app import BottleServer
from app.drivers.picklecache import PickleDBCache

app = BottleServer.create_app()


def run_app(host='localhost', port='8080'):
    PickleDBCache.init_pickle_db()
    app.run(host=host, port=port)
    PickleDBCache.close_pickle_db()


if __name__ == '__main__':
    run_app()
