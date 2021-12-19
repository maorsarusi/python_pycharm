import random
#

def randomTuple():
    a = []
    num =random.randint(3,9)
    for i in range(num):
        a.append(random.randint(1,9))
    return tuple(a)

def guessingTuple(num):
    a = []
    i=0
    while not i == num:
        x = eval(input("enter "+str(i+1)+ " number from "+str(num)+"\n"+"or -1 to out"+"\n"))
        if x>=3 and x<=9:
            a.append(x)
            i+=1
        elif x == -1:
            b=()
            return b
        else:
            print("the number must be between 3-9")           
    return tuple(a)

def nihushTest(t,N):
    a=[]
    for i in range(len(N)):
        if t[i]==N[i]:
            a.append(t[i])
        else:
            a.append('X')
    return tuple(a)

#תכנית ראשית
a = randomTuple()
b = guessingTuple(len(a))
if len(b) == 0:
  print("goodbye and thank you")
else:
    c = nihushTest(a,b)
    count = 0
    for i in range(len(c)):
        if not  c[i] =='X':
            count+=1
    precent = (count/len(a))*100
    while not precent == 100 :
          if len(b) == 0:
              print("goodbye and thank you")
          else:
              print(str(c)+"you mannaged guess: "+str(precent)+"% from the random numbers, congrats!!!")
              a = randomTuple()
              b = guessingTuple(len(a))
              if len(b) == 0:
                   print("goodbye and thank you")
                   break
              else:
                c = nihushTest(a,b)
                count = 0
              for i in range(len(c)):
                if not  c[i] =='X':
                    count+=1
              precent = (count/len(a))*100
    if precent == 100:
        print(str(c)+"you manneged guess 100% from the random numbers,you are the champion!! bye bye")
     
      
   


