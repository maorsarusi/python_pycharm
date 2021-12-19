from tailrecurse import*
from targil3_3 import tailReverseNumStr

#none tail recursion
def isPalindrome(n):
    strN = str(n)
    if len(strN) == 0:
        return True
    if len(strN)== 1:
       return True
    if not strN[0] == strN[-1]:
        return False
    return isPalindrome(int(strN[1:-1]))

#tail recursion str

@tail_call_optimized

def reversing(n,result):
    if isinstance(n,int):
        if n < 0:
            n *= -1
    strN = str(n)
    if strN == "":
        return result
    return  tailReverseNumStr(strN[:-1],result+strN[-1])

def tailiIsPalindrome(n,result):
    x = reversing(n,result)
    if x == str(n):
        return True
    else:
        return False

#תכנית ראשית
def program4():
    x = eval(input("enter the number you want to check\n"))
    string = ""
    y = isPalindrome(x)
    z = tailiIsPalindrome(x,"")
    if y == False and z == False:
        string = "it isn't a palndrome"
    else:
        string = "it's a palindrome"
    print("isPalindrom by none tail recursion on the number",x,"says that",string)
    print("isPalindrom by  tail recursion on the number",x,"says that",string)
    
    

    
#הפעלת תכנית ראשית   
if __name__ == "__main__":
    program4()
