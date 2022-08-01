def get_list_len(list):
    try:
        list.pop()
    except IndexError:
        return 0
    return 1 + get_list_len(list)


get_list_len([])
