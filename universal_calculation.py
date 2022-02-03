from sympy import isprime

label_dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
operators_dictionary = {0: '', 1: "+", 2: '-', '': 0, '+': 1, '-': 2, "GOTO": 3}
parameters_dictionary = {'Y': 1, 'X': 2, 'Z': 3}

not_equal = "≠"


def calculate_formula(x, y):
    """
    a function to calculate pair of numbers by a formula
    :param x: the left number
    :param y: the right number
    :return: the result by a formula
    """
    return monus(2 ** x * (2 * y + 1), 1)


def monus(x, y):
    """
    a function to calculate monus(minus between 2 numbers and zero if the first smaller than the second)
    :param x: the first number
    :param y: the second number
    :return:  x - y if x > y
              0     else
    """
    if x - y >= 0:
        return x - y
    return 0


def reduce_list(l):
    """
    a function to get the list of powers to the prime number
    :param l:the list of all powers
    :return:the reducing list
    """
    last = 0
    for i in range(len(l)):
        if l[i] != 0:
            last = i
    new_l = l[0:last + 1]
    prime_l = []
    for i in range(len(new_l)):
        if isprime(i):
            prime_l += [l[i]]
    return prime_l


def decomposition_into_prime(number):
    """
    a function to get the all powers for a number
    :param number: the number we gets its decomposition
    :return: a tuple of the decomposition list and counter of the decompositions

    """
    if isprime(number):
        pow_list = [0] * (number + 1)
        pow_list[number] = 1
        return pow_list, 1

    count = 0
    prime_list = [i for i in range(number) if isprime(i)]
    pow_list = [0] * (prime_list[-1] + 1)
    while True:
        for i in prime_list:
            if number % i == 0:
                if pow_list[i] == 0:
                    count += 1
                pow_list[i] += 1
                number /= i
        if number == 1:
            return pow_list, count


def print_number(l, count):
    """
    a function to print the decomposition of number by its powers
    :param l:the list of the powers
    :param count: the number of the powers that didn't 0
    :return: the decomposition of the number in the form x^y * z^w etc.
    """
    decomposition = ""
    for i in range(len(l)):
        if l[i] != 0:
            if count != 1:
                decomposition += "({}^{}) * ".format(i, l[i])
                count -= 1
            else:
                decomposition += "({}^{})".format(i, l[i])
    return decomposition


def decomposition_by_formula(number):
    """
    a function to calculate the x and y of number by the formula 2 ^ x * (2 * y + 1)
    :param number: the number we decomposing
    :return: x, y by the decomposition
    """
    number += 1
    x = 0
    y = 0
    if number % 2 != 0:
        number -= 1
    else:
        while number % 2 == 0:
            x += 1
            number //= 2
    y = number // 2
    return arrange_format(x, y)


def arrange_format(x, y):
    """
    a function to get the format <x, y>
    :param x: the right parameter
    :param y: the left parameter
    :return:  <x, y>
    """
    return "<{},{}>".format(x, y)


def extract_from_format_2(code):
    """
    a function to get the numbers of the format
    :param code: the format
    :return: the numbers extracting from the format <x, y>
    """
    code = remove_edges(code)
    splitting = code.split(",")
    x = splitting[0]
    y = splitting[1]
    return int(x), int(y)


def extract_from_format_3(code):
    """
    a function to get the 3 numbers from the pattern <a,<b,c>>
    :param code: the pattern
    :return: a tuple with a, b, c
    """
    code = remove_edges(code)
    splitting = code.split(",")
    a = int(splitting[0])
    b_c = "{},{}".format(splitting[1], splitting[2])
    b, c = extract_from_format_2(b_c)
    return a, b, c


def r(z):
    """
    a function to get the right value in the pair <x,y>
    :param z: the pair
    :return: the y
    """
    return extract_from_format_2(z)[1]


def l(z):
    """
     a function to get the left value in the pair <x,y>
    :param z: the pair
    :return: the x
    """
    return extract_from_format_2(z)[0]


def remove_edges(code):
    """
    a function to remove the first character and the last character of the string
    :param code: the string
    :return: the code without the first character and the last character
    """
    return code[1:-1]


def from_line_to_pattern(line):
    """
    a function that gets a line and became it to the pattern <a,<b,c>>
    :param line: the line from the program
    :return: the coding of the line by the pattern <a,<b,c>>
    """
    split_line = line.split()
    x = split_line[0]
    if '[' in split_line[0] or ']' in split_line[0]:
        label = remove_edges(split_line[0])
        split_label = [i for i in label]
        if len(split_label) == 1 or split_label[1] == '1':
            a = label_dictionary[label]
        else:
            a = label_dictionary[split_label[0]] + (int(split_label[1]) - 1) * 5

    else:
        a = 0
    if '+' not in split_line and '-' not in split_line:
        if "GOTO" in split_line:
            b = operators_dictionary["GOTO"]
        else:
            b = operators_dictionary['']
    else:
        if '+' in split_line:
            b = operators_dictionary['+']
        else:
            b = operators_dictionary['-']
    parameter = split_line[split_line.index('<-') - 1]
    if len(parameter) == 1:
        c = parameters_dictionary[parameter[0]]
    else:
        if parameter[0] == 'X':
            c = (int(parameter[1]) * 2)
        elif parameter[0] == 'Z':
            c = (int(parameter[1]) * 2 + 1)
    c -= 1
    return arrange_format(a, arrange_format(b, c))


def get_key(val, dictionary):
    """
    a function to get the key of a value in dictionary
    :param val: the value we looks its key
    :param dictionary: the dictionary
    :return: the key if the value is existed
    """
    for key, value in dictionary.items():
        if val == value:
            return key
    return None


def get_label(number):
    label = ""
    if number != 0:  # there is a label in the line
        num = number % 5
        if num != 0:  # its not E
            label = get_key(num, label_dictionary)
            rest = number - num
            val = rest // 5 + 1
            if val != 1:
                label += str(val)
        else:
            num = number // 5
            label = 'E'
            if num != 1:
                label += str(num)
    return label


def build_line(label, parameter, operator):
    """
    a function that build a line from all parameters
    :param label: the label if it exist
    :param parameter: the parameter the line use
    :param operator: the operator or the jump label
    :return: the line we use
    """
    line = ""
    if label != '':  # it means that we have a label
        line += "[{}]".format(label)
    if "GOTO" in operator:  # the operator isn't +-
        line += "IF {} {} 0 {}".format(parameter, not_equal, operator)
    elif operator != '':
        line += "{} <- {} {} 1".format(parameter, parameter, operator)
    else:  # not even jump
        line += "{} <- {}".format(parameter, parameter)
    return line


def from_pattern_to_line(pattern):
    """
    a function that get the pattern <a,<b,c>>
    and returns the line that belong to it
    :param pattern: <a,<b,c>>
    :return: the line
    """
    line = ""
    a, b, c = extract_from_format_3(pattern)
    label = get_label(a)
    if label != '':
        line += "[{}] ".format(label)
    c += 1
    if c == 1:  # it's Y
        parameter = get_key(c, parameters_dictionary)
    else:
        if c > 3:  # not only X or Z
            val = c // 3
        else:
            val = c
        parameter = get_key(val, parameters_dictionary)
        if c > 3:
            parameter += str(val + 1)
    if b > 2:  # jump label
        b -= 2
        operator = "GOTO " + get_label(b)
    else:
        operator = operators_dictionary[b]
    line = build_line(label, parameter, operator)

    return line


def from_line_to_number(line):
    """
    a function that gets a line and convert it to it's number
    :param line: the line to convert
    :return: the number that the line is equals to
    """
    formula = from_line_to_pattern(line)
    a, b, c = extract_from_format_3(formula)
    calc_r = calculate_formula(b, c)
    return calculate_formula(a, calc_r)


def from_number_to_line(number):
    formula = decomposition_by_formula(number)
    right = decomposition_by_formula(r(formula))
    a = l(formula)
    b = l(right)
    c = r(right)
    pattern = "<{},<{},{}>>".format(a, b, c)
    return from_pattern_to_line(pattern)


def from_godel_to_program(number):
    number += 1
    godel = decomposition_into_prime(number)[0]
    l = reduce_list(godel)
    program = []
    for num in l:
        program += [from_number_to_line(num)]
    return program

def print_program(program):
    s = ""
    for p in program:
        s += "{}\n".format(p)
    return s


def main():
    x, count = decomposition_into_prime(352)
    print(reduce_list(x))
    print(print_number(x, count))
    z = decomposition_by_formula(239)
    print(z)
    print(calculate_formula(34, 37))
    print(extract_from_format_2(z))
    print(remove_edges(z))
    print(l(z))
    print(r(z))
    t = arrange_format(33, arrange_format(12, 52))
    print(extract_from_format_3(t))
    print(from_line_to_pattern("X1 <- X1 + 1"))
    print(from_line_to_pattern("[D4] X3 <- X3 - 1"))
    print(get_key(3, label_dictionary))
    print(from_pattern_to_line("<0,<0,0>>"))
    print(from_line_to_number("X1 <- X1 + 1"))
    print(from_number_to_line(46))
    print(from_number_to_line(10))
    print()
    print(print_program(from_godel_to_program(199)))


if __name__ == '__main__':
    main()
