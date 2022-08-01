def check_palindrome_str(str):
    if len(str) <= 1:
        return True
    if str[0] == str[len(str) - 1]:
        return check_palindrome_str(str[1:len(str) - 1])
    return False
