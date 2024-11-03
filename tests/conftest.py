from pytest import fixture
from starlette.testclient import TestClient

from src.infrastructure.adapters.input.http.application import Application
from src.infrastructure.config.injector.injector import create_injector


@fixture(scope="function")
def test_client() -> TestClient:
    inject = create_injector()

    return TestClient(Application(inject).create_app())
