import uuid

from starlette.testclient import TestClient


def test_given_a_request_without_correlation_id_should_add_a_new_one_to_response_headers(
    test_client: TestClient,
):
    response = test_client.get("/")

    assert "X-Correlation-ID" in response.headers
    correlation_id = response.headers["X-Correlation-ID"]
    assert uuid.UUID(correlation_id)


def test_given_a_request_with_correlation_id_should_add_keep_the_same_in_response_headers(
    test_client: TestClient,
):
    correlation_id = str(uuid.uuid4())
    response = test_client.get("/", headers={"X-Correlation-ID": correlation_id})
    assert response.headers["X-Correlation-ID"] == correlation_id


def test_given_two_request_should_have_different_correlation_id(
    test_client: TestClient,
):
    response_1 = test_client.get("/")
    response_2 = test_client.get("/")

    assert "X-Correlation-ID" in response_1.headers
    assert "X-Correlation-ID" in response_2.headers

    assert (
        response_1.headers["X-Correlation-ID"] != response_2.headers["X-Correlation-ID"]
    )
