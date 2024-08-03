def quick_sort(arr: list[int]) -> list[int]:
    # Base case
    if len(arr) < 2:
        return arr

    # Pick an pivot
    pivot = arr[0]
    # list of int that less than pivot
    less = [i for i in arr[1:] if i <= pivot]

    # list of int that greater than pivot
    greater = [i for i in arr[1:] if i > pivot]

    # Recursive case the list will be sorted:
    return quick_sort(less) + [pivot] + quick_sort(greater)
