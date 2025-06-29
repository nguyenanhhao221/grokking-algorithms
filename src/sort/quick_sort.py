def quick_sort(arr: list[int]) -> list[int]:
    # Base c
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) - 1]
    less_than_pivot = [i for i in arr if i < pivot]
    more_than_pivot = [i for i in arr if i > pivot]

    # Recursive case
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)
