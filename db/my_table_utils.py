"""
file my_table_utils holds the static function that helped to the class "my_table"
but they aren't belongs to the instance of "my table"
"""


def from_column_to_row(columns, rows):
    """
    function from_column_to_row gets the table columns and convert the values
    to be ordered by the rows
    :param columns: the tables' values ordered by columns
    :param rows: a list with empty list in size of the columns' size
    :return: the values inserted by rows' values
    """
    if check_rows(rows):
        for i in range(len(columns)):
            for j in range(len(columns[i])):
                rows[j] += [columns[i][j]]
    else:
        new_rows = [[] for i in rows]
        return from_column_to_row(columns, new_rows)
    return rows


def check_a(line):
    """
    function check_a  gets a line and checks if every term in it is a
    :param line: a line ordered by the rows
    :return: True if everything is a and False if it didn't
    """
    true_false = []
    for att in line:
        if att[0] == "a":
            true_false += [True]
        else:
            true_false += [False]
    return all(true_false)


def check_rows(rows):
    """
    function check_rows  checks if the rows are empty
    :param rows: the values represented by rows
    :return: True if the rows are empty and False if it didn't
    """
    for l in rows:
        if l:
            return False
    return True


def find_places(dependent, R):
    """
    function find_places check the places of a dependent in R
    :param dependent: the dependent we checks
    :param R: the scheme columns
    :return: a list with the numbers by the dependents
    """
    num_list = []
    for letter in dependent:
        num_list += [R.index(letter)]
    return num_list


def incerment_value(numbers, col_values):
    """
    function incerment_value gets the values of the table
     representing by the columns
    and the numbers of the dependents  and creates
    a new list of connecting values by the dependents
    :param numbers: the numbers of the dependents
    :param col_values: the values of the dependents in the scheme column
    :return: a new list with the connected dependents (if it needed)
    """
    needed = []
    incerments = []
    inc = ""
    for i in numbers:
        needed += [col_values[i]]
    for i in range(len(col_values[0])):
        for j in range(len(needed)):
            inc += needed[j][i]
        incerments += [inc]
        inc = ""
    return incerments


def create_incerments(col_values, list_of_num):
    """
    function create_incerments create connections by the dependents for all columns
    :param col_values: the values of the table represents by the columns
    :param list_of_num: the numbers of all dependents
    :return: the connection of every dependent
    """
    increments = [[], []]
    for i in range(len(list_of_num)):
        for j in list_of_num[i]:
            if len(j) > 1:
                incerment = [incerment_value(j, col_values)]
            else:
                incerment = [col_values[j[0]]]
            increments[i] += incerment
    return increments


def find_a_b(inc_dep):
    """
    function find_a_b find the places of every a and b
    :param inc_dep: a list of values
    :return: the places for every a and b
    """
    return [i for i in range(len(inc_dep)) if inc_dep[i] == "a" or inc_dep[i] == "b"]


def splitting(right):
    """
    function splitting split a string of values of  a and b
    :param right:the string we splitting
    :return: a list with slitted values
    """
    list_of_a_b = find_a_b(right)
    if len(list_of_a_b) == 1:
        return right
    split_right = []
    for i in range(len(list_of_a_b[:-1])):
        split_right += [right[list_of_a_b[i]:list_of_a_b[i + 1]]]
    split_right += [right[list_of_a_b[-1]:]]
    return split_right


def insert_values_by_dep(right1, right2):
    """
    function insert_values_by_dep changed the values in the tables by the dependents
    :param right1: 
    :param right2:
    :return:
    """
    for i in range(len(right1)):
        if right1[i][0] == "a" or right2[i][0] != "a":
            right2[i] = right1[i]
        else:
            right1[i] = right2[i]

    for i in range(len(right2)):
        if right2[i][0] == "a" or right1[i][0] != "a":
            right1[i] = right2[i]
        else:
            right2[i] = right1[i]
    return right1, right2


def return_to_col(split_right, numbers):
    new_split_right = []
    dependents = []
    for i in range(len(numbers)):
        for j in split_right:
            dependents += [j[i]]
        new_split_right += [dependents]
        dependents = []
    return new_split_right


def insert_new_values(T, left, right, numbers):
    columns = T.get_column_values()
    split_right = []
    for i in right:
        split_right += [splitting(i)]

    for i in range(len(left)):
        for j in range(len(left)):
            if j != i:
                if len(find_a_b(right[i])) > 1 and len(find_a_b(right[j])) > 1:
                    if left[i] == left[j] and split_right[i] != split_right[j]:
                        split_right[i], split_right[j] = insert_values_by_dep(split_right[i], split_right[j])
                else:
                    if left[i] == left[j] and split_right[i] != split_right[j]:
                        if split_right[i][0] == "a" or split_right[j][0] != "a":
                            split_right[j] = split_right[i]
                        else:
                            split_right[i] = split_right[j]
    if len(numbers) != 1:
        new_col = []
        new_col = return_to_col(split_right, numbers)
        for i in range(len(new_col)):
            T.set_one_column(new_col[i], numbers[i])
    else:
        T.set_one_column(split_right, numbers[0])
    rows = []
    rows = from_column_to_row(T.get_column_values(), T.get_row_values())
    T.set_row_values(rows)
