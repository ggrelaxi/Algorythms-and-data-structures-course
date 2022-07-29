def get_degree(base, degree):
    if degree == 1:
        return base * degree
    return base * get_degree(base, degree - 1)
