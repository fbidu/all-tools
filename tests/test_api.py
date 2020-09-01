"""
Functional tests for the dummy API module
"""
import schemathesis
from fastapi.testclient import TestClient
from pytest import fixture

from api import main

# pylint: disable=redefined-outer-name
@fixture
def client() -> TestClient:
    """
    Returns a requests-like TestClient
    """
    return TestClient(main.app)


def test_decoder(client):
    """
    Tests if the 'decoder' endpoint works. That endpoint will break
    on any input that contains a non-ascii character. This test
    is deliberately ineffective, in order to highlight
    `schemathesis` capabilities on the test below.
    """
    response = client.get("/translate/maria")
    assert response.status_code == 200


# Loads the current OpenAPI schema. Not sure if
# this is the better way to connect to FastAPI
schema = schemathesis.from_dict(main.app.openapi())


@schema.parametrize()
def test_no_server_errors(case, client):
    """
    Tests if there are no 500 errors in general
    """
    response = case.call(session=client)
    case.validate_response(response)
    assert response.status_code < 500
