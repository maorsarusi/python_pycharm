import random
import fractions
PATH = r"C:\Network\work\mathematics\exercisesAll.txt"

def print_exc(f1, f2, op):
    return "{} {} {} = ".format(f1.get_fraction(), op, f2.get_fraction())

def extract_fraction(string):
    x = string[1]
    mone = int(string[1])
    mechane = int(string[-2])
    f = fractions.fraction(mone, mechane)
    f.print_fraction()
    return f

def main():
    exc_list = []
    was = []
    with open(PATH, "r") as f:
        for line in f:
          exc_list += [line[:-1]]
    while True:
        my_input = input("להגריל 2 שברים?{}".format("\n"))
        if my_input == "n":
            break
        else:
           exc_number = random.randint(0, len(exc_list))
           while exc_number in was:
               exc_number = random.randint(0, len(exc_list))
           exc = exc_list[exc_number]
           was += [exc_number]
           f1 = extract_fraction(exc[:7])
           op = exc[8]
           f2 = extract_fraction(exc[10:17])
           print(print_exc(f1, f2, op))
           while True:
               ans = input("תשובה{}".format("\n"))
               if ans == "y":
                   break
           fractions.calc_fraction(f1, f2, op)







if __name__ == "__main__":
    main()
