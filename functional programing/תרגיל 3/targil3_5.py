from tailrecurse import*

#none tail recursion
def m1(n):
    if n == 0:
        return 0
    return m1(n-1) + (n/(n+1))

#tail recursion

@tail_call_optimized

def m1Tail(n,result):
    if n == 0:
        return result
    return m1Tail(n-1,result + (n/(n+1)))

#תכנית ראשית
def program5():
    x = eval(input("enter a value\n"))
    print("the value of m1 is",m1(x))
    print("the value of m1Tail is:",m1Tail(x,0))

#הפעלת תכנית ראשית
if __name__ == "__main__":
   program5()

