from unittest.mock import Mock

from pytest import fixture

from app.queries.compare_name import CompareName
from app.use_cases.compare_name_use_case import CompareNameUseCase
from domain.model.name import Name


@fixture
def mock_name_repository():
    return Mock()


@fixture
def mock_name_comparator():
    return Mock()


@fixture
def compare_name_use_case(mock_name_repository, mock_name_comparator):
    return CompareNameUseCase(mock_name_repository, mock_name_comparator)


def test_compare_name_use_case_filtering_and_sorting(compare_name_use_case, mock_name_repository, mock_name_comparator):
    compare_name_query = CompareName(name="John Doe", threshold=0.5)
    names = [Name("1", "John Smith"), Name("2", "Johnny Doe"), Name("3", "Jane Doe")]
    similarities = [
        (names[0], 0.4),  # Below threshold, should be filtered out
        (names[1], 0.7),  # Above threshold, should be included
        (names[2], 0.6),  # Above threshold, should be included
    ]
    mock_name_repository.get_all.return_value = names
    mock_name_comparator.compare.return_value = similarities

    result = compare_name_use_case.compare_name(compare_name_query)

    assert len(result) == 2
    assert result[0][0].full_name == "Johnny Doe"
    assert result[1][0].full_name == "Jane Doe"


def test_compare_name_use_case_empty_names_list(compare_name_use_case, mock_name_repository, mock_name_comparator):
    compare_name_query = CompareName(name="John Doe", threshold=0.5)

    mock_name_repository.get_all.return_value = []
    mock_name_comparator.compare.return_value = []

    result = compare_name_use_case.compare_name(compare_name_query)

    assert result == []


def test_compare_name_use_case_no_matches_above_threshold(
    compare_name_use_case, mock_name_repository, mock_name_comparator
):
    compare_name_query = CompareName(name="John Doe", threshold=0.8)
    names = [Name("1", "John Smith"), Name("2", "Johnny Doe"), Name("3", "Jane Doe")]
    similarities = [
        (names[0], 0.5),  # Below threshold
        (names[1], 0.6),  # Below threshold
        (names[2], 0.7),  # Below threshold
    ]

    mock_name_repository.get_all.return_value = names
    mock_name_comparator.compare.return_value = similarities

    result = compare_name_use_case.compare_name(compare_name_query)

    assert result == []
