#
def evenprt(N1,N2,N3):
    if not check(N1,N2,N3):
        return []
    return [i for i in range(N1,N2+1) if zugi(i)]


def check(N1,N2,N3):
    if N2 < N1:
        print("N2 smaller than N1")
        return False
    elif N2-N1 < N3:
        print("N3 must be between N1-N2")
        return False
    return True

def zugi(i):
    return i%2==0

def printing(L,N):
    if len(L) == 0:
        return []
    print(L[0:N])
    printing(L[N:],N)
    
def printing1(L,N):
    [print(*L[i:N+i])  for i in range(0,len(L),N)]


def genEvenprt(N1,N2,N3):
    if not check(N1,N2,N3):
        return
    for i in range(N1,N2+1):
        if zugi(i):
             yield i
        
        
         
  
def main():
    x,y,z = eval(input("enter 3 numbers:\n"))
    print("printing by recursion:")
    printing(evenprt(x,y,z),z)
    print()
    print("printing by list comperhension:")
    printing1(evenprt(x,y,z),z)
    print("printing with generator:")
    print(printing(list(genEvenprt(x,y,z)),z))


main()
