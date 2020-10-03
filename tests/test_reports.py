from http import HTTPStatus

from api.constants import TOP_N_STATISTIC


def test_reports_active(client):
    response = client.get('/api/reports/active')
    assert response.status_code == HTTPStatus.OK, 'Health check failed'
    assert response.json.get('active_cases') != None, 'Missing active_cases key'
    assert len(response.json.get('active_cases')) == TOP_N_STATISTIC, 'Wrong number of top active cases'


def test_reports_confirmed(client):
    response = client.get('/api/reports/confirmed')
    assert response.status_code == HTTPStatus.OK, 'Health check failed'
    assert response.json.get('confirmed_cases') != None, 'Missing confirmed_cases key'
    assert len(response.json.get('confirmed_cases')) == TOP_N_STATISTIC, 'Wrong number of top confirmed cases'


def test_reports_deaths(client):
    response = client.get('/api/reports/deaths')
    assert response.status_code == HTTPStatus.OK, 'Health check failed'
    assert response.json.get('deaths_cases') != None, 'Missing deaths_cases key'
    assert len(response.json.get('deaths_cases')) == TOP_N_STATISTIC, 'Wrong number of top deaths cases'


def test_reports_country(client):
    response = client.get('/api/reports/country?country=US')
    assert response.status_code == HTTPStatus.OK, 'Health check failed'
    assert response.json.get('active_cases') != None, 'Missing deaths_cases key'
    assert response.json.get('confirmed_cases') != None, 'Missing deaths_cases key'
    assert response.json.get('death_cases') != None, 'Missing deaths_cases key'