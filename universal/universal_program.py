from universal.universal_calculation import *


def GOTO_F(S):
    """
    a function to get the result ofa program by the universal programing
    :param S: the value we get from the universal programing
    :return: the first godel power of the godel list
    """
    S -= 1  # this is only because in the function from_number_to_godel_list we add 1
    S = from_number_to_godel_list(S)
    Y = S[0]
    return Y


def GOTO_N(K):
    """
    a function for dummy action (N -> Nothing)
    :param K: the index of the program
    :return: K + 1
    """
    return K + 1


def GOTO_A(S, P):
    """
     a function to add 1 to the power (A -> Add)
    :param S: the result in the program by far
    :param P: the prime number to add
    :return: the multiple of S in P because X^y * X = X^y+1
    """
    return S * P


def is_divide(P, S):
    """
    a function to implement the operator |
    :param P: the prime number and the divider
    :param S: the divided
    :return: True if P|S and False if not
    """
    S % P == 0


def GOTO_M(S, P):
    """
    a function to minus 1 from one power in the godel list (M -> Minus)
    :param S: the result
    :param P: the prime we divide
    :return: S / P because X^y / X = X^y-1
    """
    return S / P


def min_line(godel, U):
    line = [i for i in range(len(godel)) if l(godel[i]) + 2 == l(
        from_number_to_format_2(U))]
    if not line:
        return 0
    return min(line)


def universal(*list_of_parameters):
    """
    the universal program to run program (an interpreter to run)
    :param list_of_parameters: the parameter of the running program - the parameters and the program number
    :return: the result of the running program
    """
    Z = list_of_parameters[0]  # the program number
    S = pi(list_of_parameters[1:])  # the program parameters
    K = 1  # the index
    godel = from_number_to_godel_list(
        Z)  # the godel list of the decomposition of the program number - represents the lines' numbers
    while True:
        if K == len(godel) + 1 or K == 0:  # check if we finished the program or if we jumping to not existing label
            return GOTO_F(S)  # finish the program
        U = r_3(from_number_to_format_3(godel[K - 1]))  # gets the <b,c> of the k instruction
        P = [[1] + [i for i in range(100 + U) if isprime(i)]][0][
            r(from_number_to_format_2(U)) + 1]  # gets the kth prime number
        if l(from_number_to_format_2(U)) == 0:  # gets the instruction type and checks if it a dummy instruction
            K = GOTO_N(K)  # goto the Nothing label
        elif l(from_number_to_format_2(U)) == 1:  # gets the instruction type and checks if it an add instruction
            S = GOTO_A(S, P)  # goto Add label
            K = GOTO_N(K)  # goto Nothing label
        elif not (is_divide(P, S)):  # checks if the parameters in different then 0
            K = GOTO_N(K)  # goto Nothing label
        elif l(from_number_to_format_2(U)) == 2:  # gets the instruction type and checks if it a minus instruction
            S = GOTO_M(S, P)  # goto Minus label
            K = GOTO_N(K)  # goto Nothing label
        else:  # it means that it is a jump instruction
            K = min_line(godel, U)  # find the instruction by search where in the program the label exists (if it's didn't exist its return 0)
    return


def pi(list_of_parameters):
    """
    a function to do the pi operation
    :param list_of_parameters: the list for the function
    :return: the result of pi operation on the list
    """
    list_of_primes = get_primes(list_of_parameters)
    list_of_powers = []
    index_parameters = 0
    for i in range(len(list_of_primes)):
        if i % 2 == 1:
            list_of_powers += [list_of_primes[i] ** list_of_parameters[index_parameters]]
            index_parameters += 1
    return multiple(list_of_powers)


def multiple(S):
    """
    a function to multiple terms in some list
    :param S: the list
    :return: the multiple of the terms
    """
    s = 1
    for i in S:
        s *= i
    return s


def main():
    program = []
    with open("program.txt", 'r') as f:
        for i in f:
            program += [from_line_to_number(i)]
    program_number = from_godel_list_to_number(program)
    print(" the program :\n {} that it's number is : {}\n result is: {}".format(print_program(from_godel_to_program(program_number)),program_number, universal(program_number)))


if __name__ == '__main__':
    main()
