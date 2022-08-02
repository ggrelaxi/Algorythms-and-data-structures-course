def generate_brackets(bracket_length):
    length = bracket_length * 2

    def gen_bracket(n, prefix):
        if n == 0:
            if isValidBracket(prefix):
                print(prefix)
        else:
            gen_bracket(n - 1, prefix + '(')
            gen_bracket(n - 1, prefix + ')')

    def isValidBracket(data):
        result = []
        counter = 0
        for i in range(len(data)):
            currentSymbol = data[i]
            if currentSymbol == "(":
                result.append(currentSymbol)
                counter += 1
            else:
                if len(result) == 0:
                    return False
                result.pop()
                counter -= 1

        return counter == 0

    return gen_bracket(length, '')


generate_brackets(4)
