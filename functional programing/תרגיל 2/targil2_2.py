def sumDigits1(n):
    return sum(perukN1(n))
#זה הולך ההבדל זה לאיזה גירסא של פירוק 
def sumDigits2(n):
    return sum(perukN2(n))

#reversed  גירסא לא מדוייקת
def perukN1(n):
    Lout = []
    while n > 10:
        n,firstDigit =perukStep(n)
        Lout.append(firstDigit)
    else:
        Lout.append(n)
    return list(reversed(Lout))

#
def perukStep(n):
    return (n//10,n%10)

# גירסא לא מדוייקת insert
def perukN2(n):
    Lout = []
    while n > 10:
        n,firstDigit =perukStep(n)
        Lout.insert(0,firstDigit)
    else:
        Lout.insert(0,n)
    return Lout

#סעיף ב
def sumDigits3(n):
    return sum(map(int,list(str(abs(n)))))

#תכנית ראשית
if __name__ == "__main__":
    while True:
        try:     
             a = int(input("enter a number posetive or negative"+"\n"))
        except ValueError:
            print("must be an integer")
            continue
        else:
          print("sumDigits1: "+str(sumDigits1(a))+" and aumDigits3: "+str(sumDigits3(a)))  
        break
