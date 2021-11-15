import sys
import os

__author__ = "Maor"

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

FILE1 = 1
FILE2 = 2

WRONG = " is wrong operator\n"


def multiple(number1, number2):
    """
    function multiple gets 2 numbers and multiple them
    :param number1: the first number
    :param number2: the second number
    :return: the multiple
    """
    return number1 * number2


def add(number1, number2):
    """
    function add gets 2 number and summarize them
    :param number1: the first number
    :param number2: the second number
    :return: the sum of the 2 numbers
    """
    return number1 + number2


def divide(number1, number2):
    """
    function divide gets 2 numbers and divide the
    :param number1: the first number
    :param number2: the second number
    :return: the division or warning alert if the second number is 0
    """
    if number2 == 0:
        return "can't divide by 0"
    return number1 / number2


def minus(number1, number2):
    """
    function minus gets 2 number and minus them
    :param number1: the first number
    :param number2: the second number
    :return: the first number minus the second number
    """
    return number1 - number2


def union(split_list):
    """
    function union gets a list and union all the parts in it
    :param split_list: the list we got
    :return: a new list with one item, that made from the whole list
    """
    if not split_list:
        return " "
    for i in split_list[1:]:
        split_list[0] += i
    return "".join(split_list[0])


def check_number(number):
    """
    function check_number gets a string and checks if it a  number or not
    :param number: the string
    :return: True if it a number and False if it didn't
    """
    if number == "":
        return False
    for i in number:
        if i not in DIGITS and not i == '-':
            return False
    return True


# operator_dictionary match between operators to function
# that calculate by the operator
operator_dictionary = {"*": multiple, "+": add, "/": divide, "-": minus}


def find_first(split_list, character):
    """
    function find_first gets a list and a character and returns
    the first appearance of the character in the list
    :param split_list: the list we looks in it
    :param character: the character we looking for
    :return: the index of the first appearance of character in split_list
    """
    for i in range(len(split_list)):
        if split_list[i] == character:
            return i
    return None


def organize_split_list(split_list):
    """
    function organize_split_list gets a list and
    returns a list that without the empty lists and
    connect between number that more than one digit
    :param split_list: the list from the file
    :return: new list without the empty lists and with
             more than one digits number if they was
    """
    corrected_list = []
    j = 0
    for i in range(0, len(split_list) - 1):
        find = find_first(split_list[j:], [])
        split = split_list[j:][0:find]
        union_number = union(split)  # union number => if the split splitting number with more than 1 digit it union it
        corrected_list += [union_number]
        j += find + 1
        if j == len(split_list):
            break
    return corrected_list


def splitting(f1):
    """
    function splitting gets a string that made from file and split it
    :param f1: the string from the file
    :return:  a list that splitting all the characters
    """
    split_list = []
    corrected_list = []
    for i in f1:
        split_list += [i.split()]
    corrected_list = organize_split_list(split_list)
    return corrected_list


def calculate_by_operator(first_number, second_number, operator):
    """
    function calculate_by_operator gets two numbers and operator
    and return the calculate of the two numbers by the operator
    :param first_number: the first number
    :param second_number: the second number
    :param operator: the operator to calculate by it
    :return: the calculation / result
    """
    if not operator in operator_dictionary.keys():
        return operator + WRONG
    else:
        return operator_dictionary[operator](first_number, second_number)


def insert_calculate(split_list):
    """
    function insert_calculate gets the split list and
    return list with the results
    :param split_list: the exercises
    :return: a list with the results
    """
    first_number = 0
    second_number = 0
    result_list = []
    operator = ""
    for i in range(0, len(split_list), 3):
        if check_number(split_list[i]):
            # if it a number with more then one digit we need to extract it from the list
            if isinstance(split_list[i], str):
                first_number = int(split_list[i])
            else:
                first_number = int(split_list[i][0])
        else:
            first_number = split_list[i]
        operator = split_list[i + 1]
        if check_number(split_list[i + 2]):
            second_number = int(split_list[i + 2])
        else:
            second_number = split_list[i + 2]
        if check_number(str(first_number)) and check_number(str(second_number)):
            result_list += [calculate_by_operator(first_number, second_number, operator)]
        else:
            result_list += ["wrong number"]
    return result_list


def write_solution(split_list, results_list):
    """
    function write_solution gets two lists of exercises and solutions
     and union them to one list
    :param split_list: the exercises list
    :param results_list: the solutions list
    :return: new list with exercises and solutions
    """
    result_index = 0
    split_list_index = 0
    list_with_solution = []
    for i in split_list:
        split_list_index += 1
        if not WRONG in str(results_list[result_index]):  # we write a string if the format didn't good
            list_with_solution.append(i)
            if split_list_index % 3 == 0:  # every 3 places we need to put '='
                list_with_solution.append("=")
                list_with_solution.append(str(results_list[result_index]))
                result_index += 1
        else:
            if split_list_index % 3 == 0:
                list_with_solution.append(results_list[result_index])
                result_index += 1
    return list_with_solution


def find_all(my_list, character):
    """
    function find_all gets a list and a character and
    gives the places that the character in the list
    :param my_list: the list we got
    :param character: the character we looking for
    :return: a list of the places that the character appears in the list
    """
    return [i for i in range(len(my_list)) if character == my_list[i]]


def create_lists_of_solutions(solution_list):
    """
    function create_lists_of_solutions gets the list of the solutions and
    create a list of lists that in every list we have and exercise and a solution
    :param solution_list: the list with the solutions
    :return: list of lists of solutions
    """
    list_of_equals_places = find_all(solution_list, "=")
    list_of_solution = []
    last_index = -2  # the index of the last character we entered to the list
    for i in list_of_equals_places:
        list_of_solution += [solution_list[last_index + 2:i + 2]]
        last_index = i
    return list_of_solution


def create_string_of_solutions(list_of_solution):
    """
    function create_string_of_solutions gets a list and returns a string
    of solution instead of list
    :param list_of_solution: the list of the solutions
    :return: a string for the file
    """
    string_of_solutions = ""
    for i in list_of_solution:
        string_of_solutions += " ".join(i) + "\n"
    return string_of_solutions


def main():
    # asserts for function

    # assert for multiple function
    assert multiple(5, 2) == 10
    assert multiple(0, 3) == 0

    # assert for add function
    assert add(122, 4) == 126
    assert add(0, 4) == 4

    # assert for divide function
    assert divide(2, 2) == 1.0
    assert divide(2, 0) == "can't divide by 0"

    # assert for minus function
    assert minus(5, 2) == 3
    assert minus(0, 3) == -3

    # assert for union function
    assert union([['1'], ['2'], ['3']]) == '123'
    assert union([]) == " "
    assert union(['1']) == '1'

    # assert for check_number function
    assert check_number("123") is True
    assert check_number("") is False
    assert check_number("777r55") is False

    # assert for find_first function
    assert find_first(["1", 'r', '5', '7', '5'], '5') == 2
    assert find_first([], "5") is None

    # assert for organize_split_list function
    assert organize_split_list([["1"], [], ["+"], [], ["6"], []]) == ['1', '+', '6']
    assert organize_split_list([]) == []

    # assert for splitting function
    assert splitting("a b c 55\n") == ['a', 'b', 'c', '55']
    assert splitting("a + t\n") == ['a', '+', 't']

    # assert for calculate_by_operator function
    assert calculate_by_operator(1, 7, "+") == 8
    assert calculate_by_operator(5, 20, "*") == 100
    assert calculate_by_operator(15, 10, '/') == 1.5
    assert calculate_by_operator(100, 90, '-') == 10
    assert calculate_by_operator(77, 99, 'k') == 'k' + WRONG

    # assert for insert_calculate function
    assert insert_calculate(['1', '+', '5']) == [6]
    assert insert_calculate(["t", '+', '7']) == ['wrong number']
    assert insert_calculate(['6', 'o', '9']) == ['o' + WRONG]

    # assert for write_solution function
    assert write_solution(['6', '+', '9'], ['15']) == ['6', '+', '9', '=', '15']
    assert write_solution(['7', 't', '9'], ['t' + WRONG]) == ['t' + WRONG]
    assert write_solution(['0', '*', 'i'], ['wrong operator']) == ['0', '*', 'i', '=', 'wrong operator']

    # assert for find_all function
    assert find_all([['4'], ['6'], ['4']], ['4']) == [0, 2]
    assert find_first([], ['8']) is None

    # assert for create_lists_of_solutions function
    assert create_lists_of_solutions(["5", '+', '7', '=', '12', '7', '*', '8', '=', '56']) == [["5", '+', '7', '=', '12'], ['7', '*', '8', '=', '56']]

    # assert for create_string_of_solutions function
    assert create_string_of_solutions([["5", '+', '7', '=', '12']]) == "5 + 7 = 12\n"

    f_string = ""
    with open(sys.argv[FILE1], 'r') as f:
        for i in f:
            f_string += i
    split_list = splitting(f_string)
    calculate_list = insert_calculate(split_list)
    solution_list = write_solution(split_list, calculate_list)
    list_of_solutions = create_lists_of_solutions(solution_list)
    solution_file = create_string_of_solutions(list_of_solutions)
    with open(sys.argv[FILE2], 'w') as file:
        file.write(solution_file)
    print("good solution")


if __name__ == "__main__":
    main()
