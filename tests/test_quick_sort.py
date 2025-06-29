import pytest

from src.sort.quick_sort import quick_sort


@pytest.mark.parametrize(
    "input, expected",
    [
        ([4, 2, 6], [2, 4, 6]),
        ([1, 0, 3, 8, 5, 16, 7], [0, 1, 3, 5, 7, 8, 16]),
    ],
)
def test_quick_sort(input: list[int], expected: int) -> None:
    output = quick_sort(input)
    assert output == expected
