def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


input = [3, 4, 1, 2]
expect = [1, 2, 3, 4]
output = insertion_sort(input)

assert expect == output
