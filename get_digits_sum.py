def get_digits_sum(number):
    if number < 10:
        return number
    return (number % 10) + get_digits_sum(number // 10)
