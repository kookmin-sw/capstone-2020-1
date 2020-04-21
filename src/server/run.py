from gevent.pywsgi import WSGIServer

from settings.settings import HOST_ADDR, SERVER_PORT, MODE
from settings.wsgi import create_wsgi

app = create_wsgi()

if __name__ == '__main__':
    if MODE == 'DEV':
        app.run(host=HOST_ADDR, port=SERVER_PORT)
    elif MODE == 'RUN':
        app = WSGIServer((HOST_ADDR, SERVER_PORT), app, log=None)
        app.serve_forever()
