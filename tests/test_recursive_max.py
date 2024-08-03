import pytest

from src.find_max import find_max


@pytest.mark.parametrize(
    "input, expected",
    [
        ([6, 4, 2, 0, 1, 3], 6),
        ([1, 2, 3], 3),
        ([8, 4, 6], 8),
    ],
)
def test_recursive_max(input: list[int], expected: int) -> None:
    output = find_max(input_list=input)
    assert output == expected
