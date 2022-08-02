def print_even(list):
    if len(list) == 0:
        return
    if list[0] % 2 == 0:
        print(list[0])
    print_even(list[1:])
