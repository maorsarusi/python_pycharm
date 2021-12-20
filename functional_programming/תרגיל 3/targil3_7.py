from tailrecurse import*
#
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
def isPrime(n, i = 2): 
  
    # Base cases 
    if (n <= 2): 
        return True if(n == 2) else False
    if (n % i == 0): 
        return False
    if (i * i > n): 
        return True 
  
    # Check for next divisor 
    return isPrime(n, i + 1) 
  
#
def LOfTwins(l):
   
    if len(l) == 1:
        return[l[0]+2]
    else:
        if isPrime(l[-1]+2):
           
            return  LOfTwins(l[:-1]) + [l[-1]+2]
        else:
            return LOfTwins(l[:-1])
#
def reversingL(l):
    if l == []:
        return []
    if len(l)==1:
        return l
    return reversingL(l[:-1])+ [l[-1]]

#

def filteringNapa(l):
   
    if len(l) == 1:
        return [l[0]]
    if isPrime(l[-1]+2):
          
            return  filteringNapa(l[:-1])+ [l[-1]]
    else:
            return filteringNapa(l[:-1])
#
def dicCreate(dic,l1,l2):
    if len(l1) == 1:
        dic[l1[0]]=l2[0]
        return dic
    else:
        dic[l1[0]]=l2[0]
        return dicCreate(dic,l1[1:],l2[1:])
    
    
    
#none tail recursion
def twinP(n):
    filNapa = reversingL(filteringNapa(napa(n)))
    twins =  reversingL(LOfTwins(napa(n)))
    dic = {}
    return dicCreate({},filNapa,twins)
#
def printingD(dictionary):
     keys = list(dictionary.keys())
     values = list(dictionary.values())
     printing(keys,values)
#
def printing(l1,l2):
    if len(l1)==0:
        return
    print("the prime is:",l1[0],"and the twin is:",l2[0])
    return printing(l1[1:],l2[1:])

#tail recursion

@tail_call_optimized

def filteringNapaTail(l,result):
    if len(l) == 0:
        return result
    if isPrime(l[-1]+2):
            result += [l[-1]]
    return  filteringNapaTail(l[:-1],result)

def LOfTwinsTail(l,result):
    if len(l) == 0:
        return result
    else:
        if isPrime(l[-1]+2):
            result += [l[-1]+2]
        return LOfTwinsTail(l[:-1],result)
#
def reversingLTail(l,result):
    if l == []:
        return result
    return reversingLTail(l[:-1],result+[l[-1]])
#
def twinPTail(n,result):
    filNapa = reversingLTail(filteringNapaTail(napa(n),[]),result)
    twins =  reversingLTail(LOfTwinsTail(napa(n),[]),result)
    dic = {}
    return dicCreateTail(dic,filNapa,twins,dic)
#
def dicCreateTail(dic,l1,l2,result):
    if len(l1) == 0:
       return result
    else:
        result[l1[0]]=l2[0]
        return dicCreateTail(dic,l1[1:],l2[1:],result)

#
def program7():
    x = eval(input("enter number\n"))
    print("the values by none tail recursion is:")
    printingD(twinP(x))
    print()
    print("the values by tail recursion is:")
    dic = twinPTail(x,[])
    printingD(dic)

    
    
if __name__ == "__main__":
    program7()
    
 
