def recursive_sum(input_list: list[int]) -> int:
    if len(input_list) == 0:
        return 0
    elif len(input_list) == 1:
        return input_list[0]
    return recursive_sum([input_list[0]]) + recursive_sum(input_list[0:])
