from typing import List, Optional


def binary_search(arr: List[int], item: int) -> Optional[int]:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    my_list: List[int] = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 7))
