import pytest

from src.recursive_count import recursive_count


@pytest.mark.parametrize(
    "input, expected",
    [
        ([2, 4, 6], 3),
        ([1, 2, 3, 4, 5, 6, 7], 7),
        ([], 0),
    ],
)
def test_recursive_sum(input: list[int], expected: int) -> None:
    output = recursive_count(input_list=input)
    assert output == expected
