def get_second_max(list):
    if len(list) < 2:
        return 0

    def inner_f(list, index, first_max, second_max):
        if index > len(list) - 1:
            return second_max
        current = list[index]

        if current > first_max:
            second_max = first_max
            first_max = current
        elif current >= second_max and current <= first_max:
            second_max = current

        return inner_f(list, index + 1, first_max, second_max)

    return inner_f(list, 0, 0, 0)
