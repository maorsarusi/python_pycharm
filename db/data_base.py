from collections import deque
from db import my_table


def check_attribute_all_keys(attribute, scheme):
    for letter in attribute:
        if letter in scheme:
            return True
    return False


def check_attribute(attribute, scheme):
    """
    function check_attribute gets an attribute and a scheme
    and checks if the attribute in the scheme
    :param attribute: the attribute we checked
    :param scheme:  the scheme we checks if the attribute in it
    :return: True if the attribute in the scheme and False if it didn't
    """
    for letter in attribute:
        if letter not in scheme:
            return False
    return True


def print_attributes(scheme):
    """
    function print_attributes gets a scheme and print it
    :param scheme: the scheme to print
    :return: the list that we print as the scheme
    """
    att_list = []
    for attribute in scheme:
        att_list += [attribute]
    print("the attributes are :{}".format(att_list))
    return att_list


def closure(X, F):
    """
    function closure gets a dependent and the dependents dictionary
    and get for the dependent the closure of it
    :param X: the dependent
    :param F: the dependents dictionary
    :return: the closure for X
    """
    V = [X]
    for Y in range(len(F[0])):
        if check_attribute(F[0][Y], "".join(V)) and not check_attribute(F[1][Y], "".join(V)):
            V += [F[1][Y]]
            for X in range(len(F[0])):
                if check_attribute(F[0][X], "".join(V)) and not check_attribute(F[1][X], "".join(V)):
                    V += [F[1][X]]
    return sorted(set("".join(V)))


def minus(R, dependents):
    """
    function minus gets a string that represent all the attribute
    and an attribute and remove it
    :param R: the whole string
    :param dependents: the character to remove
    :return: R - dependents
    """
    if not check_attribute_all_keys(dependents, R):
        return R
    elif R == dependents:
        return ''
    else:
        att_indexes = []
        for letter in dependents:
            if letter in R:
                att_indexes += [R.index(letter)]
    return "".join([i for i in R if R.index(i) not in att_indexes])


def Minimize(X, F):
    for A in X:
        if check_attribute(A, closure(minus(X, A), F)):
            X = minus(X, A)
    return X


def find_key(R, F):
    return Minimize(R, F)


def cut_between(x, y):
    for char in x:
        if char in y:
            return True
    return False


def union(x, y):
    union_attributes = ""
    for i in x:
        if i not in y:
            union_attributes += i
    return union_attributes + y


def find_all_keys(R, F):
    K = find_key(R, F)
    super_keys = []
    key_queue = deque()
    key_queue.append(K)
    keys = deque()
    keys.append(K)
    while len(key_queue) != 0:
        K = key_queue.popleft()
        for i in range(len(F[0])):
            if cut_between(K, F[1][i]):
                S = ""
                S += union(minus(K, F[1][i]), F[0][i])
                super_keys += [S]
                for J in list(keys):
                    if "".join(sorted(J)) in "".join(sorted(S)):
                        break
                    else:
                        new_key = Minimize(S, F)
                        if new_key not in keys:
                            keys.append(new_key)
                            if new_key not in key_queue:
                                key_queue.append(new_key)
    return list(keys)


def cut(x, y):
    cutter = ""
    for letter in x:
        if letter in y:
            cutter += letter
    return cutter


def isDependencyPreserving(list_of_R, F):
    z = ""
    index = 0
    index_list = 0
    for X in F[0]:
        Y = F[1][index]
        Z = X
        z = Z
        for i in list_of_R:
            index_list += 1
            d = cut(Z, i)
            y = "".join(closure(d, F))
            o = cut(y, i)
            Z_new = union(Z, o)
            if check_attribute_all_keys(Y, Z_new):
                print("the dependency {} --> {} is preserving".format(X, F[1][index]))
                index_list = 0
                break
            elif Z_new != Z:
                index_list = 0
            elif index_list == len(list_of_R):
                print("the dependency {} --> {} isn't preserving".format(X, F[1][index]))
                index_list = 0

        index += 1

    return


def print_dependencies(F):
    if F == [[], []]:
        print("empty group")
    else:
        left = F[0]
        right = F[1]
        for i in range(len(left)):
            print("{} --> {}".format(left[i], right[i]))
    return


def computeDependenciesInProjection(R, Ri, F):
    Gx = []
    Gy = []
    for X in F[0]:
        if check_attribute(X, Ri) and X not in Gx:
            Y = minus(cut("".join(closure(X, F)), Ri), X)
            if Y != '':
                Gx += [X]
                Gy += [Y]

    return [Gx, Gy]


def computeMinimalCover(F):
    G = []
    left = []
    right = []
    for i in range(len(F[0])):
        for Y in F[1][i]:
            left += [F[0][i]]
            right += [Y]
    G = [left, right]
    print_dependencies(G)
    Ga = []
    lefta = []
    righta = []
    for i in range(len(G[0])):
        Y = G[1][i]
        X = G[0][i]
        for B in X:
            F_new = remove_dependent(X, Y, G)
            m = minus(X, B)
            c = closure(m, F_new)
            if Y in "".join(c) and len(G[0][i]) != 1:
                G[0][i] = m
        lefta += [G[0][i]]
        righta += [G[1][i]]
    ga = [lefta, righta]
    print_dependencies(ga)


def remove_dependent(X, Y, F):
    index = F[0].index(X)
    rest_left = []
    rest_right = []
    while True:
        if F[1][index] == Y:
            left = F[0][:index] + F[0][index + 1:]
            right = F[1][:index] + F[1][index + 1:]
            all_left = rest_left + left
            all_right = rest_right + right
            return [all_left, all_right]
        else:
            rest_left += F[0][:index + 1]
            rest_right += F[1][:index + 1]
            F[0] = F[0][index + 1:]
            F[1] = F[1][index + 1:]
            index = F[0].index(X)


def main():
    left = []
    right = []
    scheme = input("Please insert the attributes in this scheme\n")
    while True:
        left_attribute = input("Please insert the left attribute, if you want to stop insert 0\n")
        if left_attribute == '0':
            break
        right_attribute = input("Please insert the right attribute\n")
        if not check_attribute(left_attribute, scheme) or not check_attribute(right_attribute, scheme):
            print(" At least one of the attributes not in the scheme, please try again\n")
        else:
            left += [left_attribute]
            right += [right_attribute]
            print("attributes insert correctly!\n")
    scheme_list = print_attributes(scheme)
    dependents = [left, right]
    print("the dependents are:")
    print_dependencies(dependents)
    for attribute in scheme:
        print("{}+ is :{}".format(attribute, "".join(closure(attribute, dependents))))
    for key in dependents[0]:
        if key not in scheme_list:
            print("{}+ is :{}".format(key, "".join(closure(key, dependents))))
    print("the first key to find is: {}".format(find_key(scheme, dependents)))
    all_keys = find_all_keys(scheme, dependents)
    print("all keys for this scheme : {}".format(all_keys))
    Demolitions = []
    while True:
        r = input("Please insert the Demolitions, to stop insert 0\n")
        if r == '0':
            break
        Demolitions += [r]

    T = my_table.my_Table(scheme, Demolitions)
    T.insert_values()
    print("Table after initialize")
    T.print_table()
    print()
    print(T.chase_table(dependents))
    print(isDependencyPreserving(Demolitions, dependents))


if __name__ == "__main__":
    main()
