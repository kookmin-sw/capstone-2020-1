from db import Database
from models.highlight import Predict


def test_get_predict(client):
    data = {
        'url': 'asdfawefasdf'
    }
    res = client.get('api/predict', query_string=data)
    assert res.status_code == 400
    data = {
        'url': 'http://vod.afreecatv.com/PLAYER/STATION/53773494'
    }
    res = client.get('api/predict', query_string=data)
    assert res.status_code == 200

    with Database() as db:
        query = db.query(Predict).filter(
            Predict.url == data['url']
        ).first()

        if not query:
            raise ('NotConnectDatabase')
