import pytest
from fastapi.testclient import TestClient
import json
from app.main import app
import definitions


@pytest.fixture
def client():
    yield TestClient(app)


def test_read_metrics(client):
    response = client.get("/performance-metrics/")
    assert response.status_code == 200
    with open(definitions.READ_METRICS_RESPONSE) as f:
        res = json.load(f)
    assert response.json() == res


def test_query_metrics(client):
    with open(definitions.REQUEST_FILE_1) as rfile:
        req = json.load(rfile)
    response = client.post("/performance-metrics/query", json=req)
    assert response.status_code == 200
    with open(definitions.RESPONSE_FILE_1) as f:
        res = json.load(f)
    assert response.json() == res
