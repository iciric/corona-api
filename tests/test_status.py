from http import HTTPStatus


def test_status(client):
    response = client.get('/status/')
    assert response.status_code == HTTPStatus.OK, 'Health check failed'
    assert response.json == {'message': 'Running'}, 'Improper response'
