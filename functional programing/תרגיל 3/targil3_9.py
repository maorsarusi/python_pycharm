from tailrecurse import*
from targil3_1 import program1
from targil3_2 import program2
from targil3_3 import program3
from targil3_4 import  program4
from targil3_5 import  program5
from targil3_6 import program6
from targil3_7 import program7
from targil3_8 import program8

#none tail recursion

def createValuesDic(l,l1):
   if len(l) == 0:
       return []
   return createValuesDic(l[:-1],l1[:-1])+[(l[-1],l1[-1])]

def createDictionary(l):
    return dict(l)
def checkInput(x,d):
    if x not in list(range(0,9)):
        print("must be between 1-8, 0 to exit")
        x = eval(input("input a number between 1-8,to exit print 0\n"))
        checkInput(x,d)
    elif x == 0:
        print("byeBye")
        return
    else:
       d[x]()
       x = eval(input("input a number between 1-8,to exit print 0\n"))
       checkInput(x,d)

@tail_call_optimized
       
#tail recursion

def createDictionaryTail(l,l1,result):
    if len(l) == 0:
        return result
    return createDictionaryTail(l[1:],l1[1:],result+[(l[0],l1[0])])


        
def main():
    lKeys = list(range(1,9))
    lValues = [program1,program2,program3,program4,program5,program6,program7,program8]
    recursion = eval(input("input  t or T to create the menu by tail recursion and every thing else creat the menu by none recursion,must be a string\n"))
    if  recursion == 'T' or recursion == 't':
         print("you choose tail")
         dictTargil3= createDictionary(createDictionaryTail(lKeys,lValues,[]))
    else:
         print("you choose none tail")
         dictTargil3= createDictionary(createValuesDic(lKeys,lValues))
        
        
    print("input a number between 1-8,to exit print 0")
    print("to find penta number for value press 1")
    print("to find sum of number's digits press 2")
    print("to find the reverse for number press 3")
    print("to find if a number is a palindrome press 4")
    print("to find the value of  i / (i +1) from 0 to thhis number  press 5")
    print("to find the value of  ((-1**(i+1))/((2*i)-1)) from 0 to this number  press 6")
    print("to find a list of twins number till this number press 7")
    print("to combine 3 dictionary to a one press 7")
    x = eval(input())
    checkInput(x,dictTargil3)
    


main()





