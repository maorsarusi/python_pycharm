#
# eratosthenes.py
# The Eratosthenes' algorithm
#
from functools import reduce
def napa(N):
    rishoni = [True]*N
    rishoni[0] = False
    # make rishoni to be an array of True values for prime numbers
    for i in range(2,N):
        if rishoni[i]:
            for mlt in range(i*2,N,i):
               rishoni[mlt]=False
    res = []
    for i, item in enumerate(rishoni):
       if item:
         res.append(i)
    return res

#
def isPrime(n):
    if n == 1:
        return True
    elif n==0:
        return False
    return not any(map(lambda i :  n % i == 0,range(2,n)))
#
def napaFiltering(n):
    return list(filter(lambda i : isPrime(i+2),napa(n)))
#
def napaFilterinPlus2(n):
    return list(map(lambda i : napaFiltering(n)[i]+2,range(len((napaFiltering(n))))))

#סעיף א
def twinp(n):
  return dict(zip(napaFiltering(n),napaFilterinPlus2(n)))

def Printing(d,length):
    if length==0:
         return
    Printing(d,length-1)
    print("the prime is: "+str(list(d.keys())[length-1])+" and the twin is: "+str(list(d.values())[length-1]))
#
def program3():
    x = eval(input("enter a value\n"))
    Printing(twinp(x),len(twinp(x)))

#תוכנית ראשית
if __name__ == "__main__":
    program3()


