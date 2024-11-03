import json
import uuid

from starlette.testclient import TestClient

from tests.resources.factories.infrastructure.acl.dto.update_account_request_dto_factory import (
    UpdateAccountRequestDtoFactory,
)
from tests.resources.factories.infrastructure.acl.dto.insert_account_request_dto_factory import (
    InsertAccountRequestDtoFactory,
)


def test_given_no_accounts_when_listing_all_should_return_empty_list(
    test_client: TestClient,
):
    response = test_client.get("/accounts")
    assert response.status_code == 200
    assert response.json()["accounts"] == []


def test_given_no_accounts_when_finding_one_should_return_not_found(
    test_client: TestClient,
):
    response = test_client.get(f"/accounts/{uuid.uuid4()}")
    assert response.status_code == 400
    assert response.json()["message"] == "Account not found"


def test_given_an_inserted_account_when_listing_all_should_return_a_non_empty_list(
    test_client: TestClient,
):
    request = InsertAccountRequestDtoFactory.create()

    response = test_client.post("/accounts", json=request.model_dump())
    list_response = test_client.get("/accounts")

    assert response.status_code == 200
    assert response.json()["contact_information"]["email"] == request.email
    assert len(list_response.json()["accounts"]) == 1


def test_given_an_existing_account_when_deleting_should_return_ok(
    test_client: TestClient,
):
    insert_request = InsertAccountRequestDtoFactory.create()
    test_client.post("/accounts", json=insert_request.model_dump())

    list_response = test_client.get("/accounts")
    account_id = list_response.json()["accounts"][0]["id"]

    delete_response = test_client.delete(f"/accounts/{account_id}")
    response_list = test_client.get("/accounts")

    assert delete_response.status_code == 200
    assert len(response_list.json()["accounts"]) == 0


def test_given_no_accounts_when_updating_should_return_error(
    test_client: TestClient,
):
    request = UpdateAccountRequestDtoFactory.create()
    response = test_client.put(f"/accounts/{request.id}", json=json.loads(request.model_dump_json()))

    assert response.status_code == 400


def test_given_an_existing_account_when_updating_should_return_ok(
    test_client: TestClient,
):
    insert_request = InsertAccountRequestDtoFactory.create(email="old@email.com")
    test_client.post("/accounts", json=json.loads(insert_request.model_dump_json()))

    list_response = test_client.get("/accounts")
    account_id = list_response.json()["accounts"][0]["id"]

    update_request = UpdateAccountRequestDtoFactory.create(id=account_id, email="new@email.com")

    update_response = test_client.put(f"/accounts/{account_id}", json=json.loads(update_request.model_dump_json()))
    modified_account = test_client.get(f"/accounts/{account_id}")

    assert update_response.status_code == 200
    assert modified_account.json()["id"] == str(update_request.id)
    assert modified_account.json()["contact_information"]["email"] == "new@email.com"
