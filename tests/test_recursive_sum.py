import pytest

from src.recursive_sum import recursive_sum


@pytest.mark.parametrize(
    "input, expected",
    [
        ([2, 4, 6], 12),
        ([1, 2, 3], 6),
        ([], 0),
    ],
)
def test_recursive_sum(input: list[int], expected: int) -> None:
    output = recursive_sum(input_list=input)
    assert output == expected
