def print_even_index(list):
    length = len(list)

    def inner_f(index):
        if length == 0 or index > length:
            return
        if index % 2 == 0:
            print(list[index])
        inner_f(index + 1)

    inner_f(0)
