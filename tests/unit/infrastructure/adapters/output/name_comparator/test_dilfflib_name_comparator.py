from difflib import SequenceMatcher

from pytest import fixture

from app.ports.output.name_comparator.name_comparator import NameComparator
from domain.model.name import Name
from infrastructure.adapters.output.name_comparator.difflib_name_comparator import DiffLibNameComparator


@fixture
def comparator() -> NameComparator:
    return DiffLibNameComparator()


def test_given_the_same_name_should_return_1_similarity(comparator: NameComparator) -> None:
    name = "John Doe"
    names = [Name("1", "John Doe")]
    expected_similarity = 1.0

    result = comparator.compare(name, names)

    assert len(result) == 1
    assert result[0][0].full_name, "John Doe"
    assert result[0][1] == expected_similarity


def test_given_similar_names_should_return_more_then_half_similarity(comparator: NameComparator):
    name = "Johnathan Doe"
    names = [Name("1", "John Doe")]

    result = comparator.compare(name, names)

    assert len(result) == 1
    assert result[0][0].full_name == "John Doe"
    assert result[0][1] > 0.5


def test_given_three_names_should_be_get_similarity_for_each_one(comparator: NameComparator):
    name = "John Doe"
    names = [Name("1", "Jane Smith"), Name("2", "Johnny Doey"), Name("3", "John Doe")]

    result = comparator.compare(name, names)

    assert len(result) == 3
    assert result[0][1] < result[1][1] < result[2][1]


def test_given_empty_list_should_return_empty_list(comparator: NameComparator):
    name = "John Doe"
    names = []

    result = comparator.compare(name, names)

    assert len(result) == 0
