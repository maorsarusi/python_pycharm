def listOfTuples(x):
    length=len(x)
    i=0
    L=[]
    while i<length:         
            if isinstance(x[i],tuple):
                L.append(x[i])
            i=i+1
    return L
def tupleOfLists(x):
    length=len(x)
    i=0
    L=[]
    while i<length:         
            if isinstance(x[i],list):
                L.append(x[i])
            i=i+1
    M=tuple(L)
    return M
def listOfStrings(x):
    length=len(x)
    i=0
    L=[]
    while i<length:         
            if isinstance(x[i],str):
                L.append(x[i])
            i=i+1
    return L

def ListOfNumbs(x):
    length=len(x)
    i=0
    L=[]
    while i<length:         
            if isinstance(x[i],int) or isinstance(x[i],float)or isinstance(x[i],complex):
                L.append(x[i])
            i=i+1
    return L
     
#תוכנית ראשית

L=[1,2,'a',(11,2,'b'),[22,'c'],(33,),['d'],'e']
print("list of tuples are:")
print(listOfTuples(L))
print ("tuples of list are:")
print(tupleOfLists(L))
print("list of strings are:")
print(listOfStrings(L))
print("List of numbers are:")
print(ListOfNumbs(L))


