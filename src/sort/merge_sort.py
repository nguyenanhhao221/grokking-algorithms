def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    mid_index = len(nums) // 2
    left_arr = nums[:mid_index]
    right_arr = nums[mid_index:]
    sorted_left = merge_sort(left_arr)
    sorted_right = merge_sort(right_arr)
    return merge(sorted_left, sorted_right)


def merge(first: list[int], second: list[int]) -> list[int]:
    final: list[int] = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] > second[j]:
            final.append(second[j])
            j += 1
        else:
            final.append(first[i])
            i += 1
    if i < len(first):
        final = final + first[i:]
    if j < len(second):
        final = final + second[j:]
    return final


test_cases: list[tuple[list[int], list[int]]] = [
    # (input, expected_output)
    ([3, 2, 1], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1], [1]),
    ([], []),
    ([2, 1], [1, 2]),
    ([1, 3, 2, 3, 1], [1, 1, 2, 3, 3]),
    ([0, -1, 5, 3, -2], [-2, -1, 0, 3, 5]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
]

for idx, (input_list, expected) in enumerate(test_cases):
    result = merge_sort(input_list)
    assert result == expected, (
        f"Test case {idx + 1} failed: input={input_list}, expected={expected}, got={result}"
    )
