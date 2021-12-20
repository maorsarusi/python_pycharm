#סעיף א
#non tail recursian
def sumDigit1(n):
    return mySum1(createLst1(n))

#
def mySum1(L):
    if L==[]:
        return 0
    return mySum1(L[1:])+L[0]

#
def createLst1(n):
    if n//10 == 0:
        return[n]
    else:
        return createLst1(n//10)+[n%10]
    
#tail recursian

def mySum2(L,result):
    if L==[]:
        return result
    return mySum2(L[1:],result+L[0])

#
def createLst2(n):
    if n//10 == 0:
        return[n]
    return createLst2(n//10)+[n%10]

#סעיף ב
def createLst3(n):
    if n=="":
        return 0
    else:
        return createLst3(n[1:])+n[0]
#
def sumDigit3(n):
    return mySum2(createLst2(n),0)

#תכנית ראשית
def program2():
    x =  eval(input("enter a number"+"\n"))
    print("sum digits of the number:",x,"by none tail rcursion is:",sumDigit1(x))
    print("sum digits of the number:",x,"by  tail rcursion is:",sumDigit3(x))
  




#הפעלת תכנית ראשית    
if __name__ == "__main__":
    program2()
 
