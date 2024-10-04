import pytest


@pytest.mark.functional
def test_home_endpoint_response(client):
    response = client.get(path="/")
    assert 200 == response.status_code
    assert ":D" in str(response.content)


@pytest.mark.functional
@pytest.mark.django_db
def test_form_endpoint_response(client):
    response = client.get(path="/data_form")
    assert 200 == response.status_code
    assert "Enter Data" in str(response.content)


@pytest.mark.functional
@pytest.mark.django_db
def test_data_list_endpoint_response(client):
    response = client.get(path="/data_list")
    assert 200 == response.status_code
    assert "Recorded Data" in str(response.content)
