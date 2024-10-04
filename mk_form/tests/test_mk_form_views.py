import pytest


@pytest.mark.functional
def test_home_endpoint_response(client):
    response = client.get(path="/")
    assert 200 == response.status_code
    assert ":D" in str(response.content)
