def find_max(input_list: list[int]) -> int:
    if len(input_list) == 2:
        return input_list[0] if input_list[0] > input_list[1] else input_list[1]
    sub_max = find_max(input_list[1:])
    return input_list[0] if sub_max < input_list[0] else sub_max
