def get_list_len(list):
    if len(list) == 0:
        return 0
    list.pop()
    return 1 + get_list_len(list)


get_list_len([])
