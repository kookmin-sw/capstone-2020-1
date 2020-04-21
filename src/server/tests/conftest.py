from pytest import fixture

from settings.wsgi import create_wsgi

app = create_wsgi()


@fixture()
def client():  # pytest용 클라이언트
    return app.test_client()
