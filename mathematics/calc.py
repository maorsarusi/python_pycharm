from mathematics import fractions

PATH = r"C:\Network\work\mathematics\exercisesAll.txt"

def main():
    y = []
    with open(PATH, "r") as f:
        for i in f:
            x = i.split()
            f1 = fractions.fraction(int(x[0][1]), int(x[2][0]))
            f2 = fractions.fraction(int(x[4][1]), int(x[6][0]))
            op = x[3]
            if op == "+":
                f3 = f1.add_fraction(f2)
            if op == "*":
                f3 = f1.mul_fraction(f2)
            if op == "-":
                f3 = f1.sub_fraction(f2)
            if op == ":":
                f3 = f1.div_fraction(f2)
            mone = "({}".format(f3.get_mone())
            mechane = "{})".format(f3.get_mechane())
            x += [mone]
            x += "/"
            x += [mechane]
            x += "\n"
            y += x
    with open(PATH, "w") as f:
        for i in y:
            f.write(i)
            if not i == "\n":
                f.write(" ")


if __name__ == '__main__':
    main()