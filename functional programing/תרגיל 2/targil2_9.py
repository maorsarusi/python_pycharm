from targil2_1 import prtPentNum1
from targil2_2 import sumDigits1
from targil2_3 import reverseNum1
from targil2_4 import  program
from targil2_5 import  program1
from targil2_6 import program2
from targil2_7 import  program3
from targil2_8 import add3dicts


#
names = [1,2,3,4,5,6,7,8]
values = [prtPentNum1,sumDigits1,reverseNum1,program,program1,program2,program3,add3dicts]
dTargil2 = dict(zip(names,values))
print("input a number between 1-8,to exit print 0")
print("to find penta number for value press 1")
print("to find sum of number's digits press 2")
print("to find the reverse for number press 3")
print("to find if a number is a palindrome press 4")
print("to find the value of  i / (i +1) from 0 to thhis number  press 5")
print("to find the value of  ((-1**(i+1))/((2*i)-1)) from 0 to thhis number  press 6")
print("to find a list of twins number till this number press 7")
print("to combine 3 dictionary to a one press 7")
x = eval(input())
while not x == 0:
        if x ==1:
             dTargil2[1]()
        elif x == 2:
            y = eval(input("enter the value of the number you want to sum its digit\n"))
            print(dTargil2[2](y))
        elif x == 3:
             y = eval(input("enter the value of the number you want to see in reverse\n"))
             print(dTargil2[3](y))
        elif x == 4:
            dTargil2[4]()
        elif x == 5:
           dTargil2[5]()
        elif x == 6:
            dTargil2[6]()
        elif x == 7:
           dTargil2[7]()
        elif x == 8:
             d1 = dict([(1,'a'),(3,'d'),(5,'e')])
             d2 = dict([(1,'b'), (3,(11,22)), (7,'f'), (4,'q')])
             d3 = dict([(2,'c'), (3,'x'), (4,'t'), (8,'g')])
             print (dTargil2[8](d1,d2,d3))
        elif  not x == 0:
            print("must be between 0-8")
        x = eval(input("input a number between 1-8,to exit print 0\n"))
print("bye")
