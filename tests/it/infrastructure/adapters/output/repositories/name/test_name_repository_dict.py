from unittest.mock import patch, mock_open

from infrastructure.adapters.output.repositories.name.name_repository_dict import NameRepositoryDict


def test_init():
    repo = NameRepositoryDict()

    assert len(repo.get_all()) == 5000
