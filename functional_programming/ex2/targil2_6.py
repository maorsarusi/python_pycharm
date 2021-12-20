#סעיף א
def pi(n):
    return 4*sum(map(lambda i : ((-1**(i+1))/((2*i)-1)),range(1,n)))

#סעיף ב
def printing(x):
    if x == 0:
        return
    printing(x-1)
    print("the value is:",x,"and the value of pi is:",pi(x))

#
def checkValue():
    x = eval(input("enter an integer number"+"\n"))
    if not isinstance(x,int):
        print("must be an integer")
        checkValue()
        return
    else:
        return x
#
def program2():
    x = checkValue()
    printing(x)
#
if __name__ == "__main__":
   program2()

