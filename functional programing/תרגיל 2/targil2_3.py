#סעיף א
def reverseNum1(n):
    strN = str(abs(n))
    return int(strN[::-1])

#סעיף ב
def reverseNum2(n):
    lstN =str(abs(n))
    return list(reversed(lstN))
    
#סעיף ג
def checkValue():
     x = int(input("Enter an integer number"+"\n"))
     if not type(x) == type(1):
        print("must be an integer"+"\n")
     else:
        return x

#תוכנית ראשית  
if __name__ == "__main__":
  x = checkValue()
  print("the value by reverseNum1 is: "+ str(reverseNum1(x)))
  print("the value by reverseNum2 is: "+ str(reverseNum2(x)))
  

  
    

