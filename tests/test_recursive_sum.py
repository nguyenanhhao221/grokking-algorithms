from src.sort.recoursive_sum import recursive_sum


def test_recursive_sum():
    input = [2, 4, 6]
    expected = 12

    output = recursive_sum(input_list=input)
    assert output == expected
