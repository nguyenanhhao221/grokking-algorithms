import pytest

from src.binary_search import binary_search


@pytest.mark.parametrize(
    "sorted_list, target, expected_output",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, None),
        ([10, 20, 30, 40, 50], 10, 0),
        ([10, 20, 30, 40, 50], 50, 4),
        ([1, 3, 5, 7, 9], 2, None),
        ([], 1, None),
        ([1], 1, 0),
        ([1], 0, None),
        ([2, 4, 6, 8, 10], 4, 1),
        ([2, 4, 6, 8, 10], 5, None),
    ],
)
def test_binary_search(
    sorted_list: list[int], target: int, expected_output: int | None
):
    output = binary_search(sorted_list, target)
    assert output == expected_output
