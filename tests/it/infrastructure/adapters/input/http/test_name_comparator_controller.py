import json

from starlette.testclient import TestClient

from infrastructure.acl.dto.requests.compare_name_request_dto import CompareNameRequestDto


def test_given_empty_string_should_return_empty_dict(test_client: TestClient) -> None:
    response = test_client.post("/names", json=CompareNameRequestDto(name="").model_dump())

    assert response.status_code == 200
    assert response.json() == {}


def test_given_out_of_bounds_threshold_should_return_validation_error(test_client: TestClient) -> None:
    response = test_client.post("/names", json=json.dumps({"name": "Juan González", "threshold": 2}))

    assert response.status_code == 422


def test_given_valid_request_should_return_validation_ok(test_client: TestClient) -> None:
    response = test_client.post("/names", json=CompareNameRequestDto(name="Juan González", threshold=1).model_dump())

    assert response.status_code == 200
    assert len(response.json()) == 7
