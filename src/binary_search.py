def binary_search(sorted_arr: list[int], item: int) -> int | None:
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    my_list: list[int] = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 7))
