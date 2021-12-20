import random


#

def randomTuple():
    """
    a function to create a tuple of random numbers between 1, 9
    :return:  a random tuple
    """
    a = []
    num = random.randint(3, 9)
    for i in range(num):
        a.append(random.randint(1, 9))
    return tuple(a)


def guessingTuple(num):
    """
    a function to guess the results in the tuple
    :param num: the length of the guessing tuple
    :return: a tuple with the guessing
    """
    a = []
    i = 0
    while not i == num:
        x = eval(input("enter " + str(i + 1) + " number from " + str(num) + "\n" + "or -1 to out" + "\n"))
        if 3 <= x <= 9:
            a.append(x)
            i += 1
        elif x == -1:
            b = ()
            return b
        else:
            print("the number must be between 3-9")
    return tuple(a)


def guessingTest(t, N):
    """
    a function to check the guessing
    :param t: the guess tuple
    :param N: the random tuple
    :return: a tuple with the results
    """
    a = []
    for i in range(len(N)):
        if t[i] == N[i]:
            a.append(t[i])
        else:
            a.append('X')
    return tuple(a)


# תכנית ראשית
def main():
    a = randomTuple()
    b = guessingTuple(len(a))
    if len(b) == 0:
        print("goodbye and thank you")
    else:
        c = guessingTest(a, b)
        count = 0
        for i in range(len(c)):
            if not c[i] == 'X':
                count += 1
        percentage = (count / len(a)) * 100
        while not percentage == 100:
            if len(b) == 0:
                print("goodbye and thank you")
            else:
                print(str(c) + "you mannaged guess: " + str(percentage) + "% from the random numbers, congrats!!!")
                a = randomTuple()
                b = guessingTuple(len(a))
                if len(b) == 0:
                    print("goodbye and thank you")
                    break
                else:
                    c = guessingTest(a, b)
                    count = 0
                for i in range(len(c)):
                    if not c[i] == 'X':
                        count += 1
                percentage = (count / len(a)) * 100
        if percentage == 100:
            print(str(c) + "you maneged guess 100% from the random numbers,you are the champion!! bye bye")


if __name__ == '__main__':
    main()