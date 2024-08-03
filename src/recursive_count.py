def recursive_count(input_list: list[int]) -> int:
    """Recursive function to count the number of items in a list”"""
    if input_list == []:
        return 0
    return 1 + recursive_count(input_list[1:])
