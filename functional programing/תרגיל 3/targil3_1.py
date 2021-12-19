from tailrecurse import*

def pentaNumRangeNone(n1,n2):
    getPentaNum = lambda i :  i*(3*i-1)/2
    return pentaLst(getPentaNum,n1,n2)

# non tail recursion
def pentaLst(getPentaNum,n1,n2):
    if n1 == n2:
        return []
    else:
        return  [getPentaNum(n1)]+ pentaLst(getPentaNum,n1+1,n2) 

# tail recursion

@tail_call_optimized

#
def pentaNumRangetail(n1,n2):
    getPentaNum = lambda i :  i*(3*i-1)/2
    return tailPentaLst(getPentaNum,n1,n2,[])

def tailPentaLst(getPentaNum,n1,n2,result):
    if(n1 == n2):
        return result
    else:
        return tailPentaLst(getPentaNum,n1+1,n2,result +[getPentaNum(n1)])

#
def get2Nums():
     n1 = int(input("enter the value of  n1:"))
     n2 = int(input("enter the value of  n2 it must be bigger than n1:"))
     if isinstance(n1,int) and n1>0 and isinstance(n2,int) and n1 < n2:
          return n1,n2
     return False

#תכנית ראשית
def program1():
    n1,n2 = get2Nums()
    print("none tail: ",pentaNumRangeNone(n1,n2))
    print("     tail: ",pentaNumRangetail(n1,n2))
    


    
#הפעלת תכנית ראשית
if __name__ == "__main__":
  program1()
