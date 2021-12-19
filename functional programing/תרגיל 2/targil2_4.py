#
def isPalindrome(n):
    return n == reverseNum(n)
#  
def reverseNum(n):
    strN = str(n)
    return int(strN[::-1])

#
def myPrt(isPal):
    if isPal:
        print("it is a palindrome")
    else:
        print("it isn't a palindrome")
    return
#
def program():
    n = eval(input("enter positive or negative number"+"\n"))
    if isinstance(n,int) and n != 0:
        if n > 0:
            myPrt(isPalindrome(n))
            
        elif n < 0:
            myPrt(isPalindrome(n*-1))
        else:
            print("the input must be an integer")
            

        
#הרצה של התרגיל שנוכל להשתמש בו כמודול
if __name__ == "__main__":
            program()
