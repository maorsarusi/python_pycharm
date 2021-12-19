from functools import reduce

def convertToBinary(num):
    if num == 0:
        return [] 
    elif num % 2 == 0:
         return convertToBinary(num//2)+[0]
    else:           
      return convertToBinary(num//2)+[1]

def zerosList(length):
    return [0 for i in range (length)]

def enterZeroList(l1,l2):
    if len(l1) > len(l2):
        return l1,zerosList(abs(len(l1)-len(l2)))+l2
    else:
         return zerosList(abs(len(l1)-len(l2)))+l1,l2

def createAndNumber(l1,l2):
    if len(l2) == 0:
        return []
    elif  l1[0] == 1 and l2[0] == 1 :
        return [1] + createAndNumber(l1[1:],l2[1:])
    elif l1[0] == 0 or l2[0] == 0:
        return [0] + createAndNumber(l1[1:],l2[1:])
def convertToDecimalpow(l):
    if len(l) == 0:
        return []
    return [l[0]*2 ** (len(l)-1)] + convertToDecimalpow(l[1:])

def convertToDecimal(l):
    return reduce(lambda x,y : x + y,convertToDecimalpow(l))

def convertToString(l):
    if len(l) == 0:
        return ""
    return str(l[0]) + convertToString(l[1:])

def logicAndBetweenNumbers(x,y):
    x1 = convertToBinary(x)
    y1 = convertToBinary(y)
    x1,y1 = enterZeroList(x1,y1)
    z1 = createAndNumber(x1,y1)   
    print("the first number in binary is:",convertToString(x1),"(decimal:",x,")")
    print("the second number in binary is:",convertToString(y1),"(decimal:",y,")")
    print("the 'and' between those in binary is:",convertToString(z1))
    return "and the value of it in decimal is :" +str(convertToDecimal(z1))
        


        
        

def main():
    x,y = eval(input("enter 2 numbers\n"))    
    print(logicAndBetweenNumbers(x,y))
    return
main()
        
