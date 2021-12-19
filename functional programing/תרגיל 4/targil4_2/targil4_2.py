#'פונקציות לסעיף א
#method to create a dictionary from a sentence and to check if it wroten with no numbers
#הערה:בשביל דיוק פונקציונאלי עדיף הכל בשורה אחת
def treatLine(lineNr,line):
    keys = line.split()
    vowels =  listOfSentence(keys,crateListVByWord)
    tup = enterToATuple(vowels)
    consonantbm = listOfSentence(keys,createListbmByWord)
    tup += enterToATuple(consonantbm)
    consonantnz = listOfSentence(keys,createListnzByWord)
    tup += enterToATuple(consonantnz)
    values = list(zip(*[(item) for item in tup]))
    d = createDic(keys,values,{})
    return tuple([lineNr])+(d,)


    
#method to check if it wroten with no numbers 
def checkAllLetters(line):
    if not all([False for i in range(0,len(line)) for j in range(0,len(line[i])) if line[i][j] <= '9' and line[i][j] >='1' ]):
       return -1
    return 1

#method to create a list of vowels from a word 
def crateListVByWord(word,vowels = ['a','i','e','o','u']):
    return list([word[i]  for i in range(0,len(word)) if word[i].lower() in vowels ])

#general method to create a list of something from a sentence by a "func"  
def listOfSentence(line,func):
    if len(line) == 0:
        return []
    return listOfSentence(line[:-1],func)+[func(line[-1])]


#method to create a list of letters from b-n a word 
def  createListbmByWord(word,vowels = ['a','i','e','o','u']):
    return list([word[i]  for i in range(0,len(word)) if word[i].lower()<='m' and word[i].lower()>='a' and not word[i].lower() in vowels])

#method to create a tuple from some lists
def enterToATuple(L,x =[]):
    return tuple([L]+x)

#method to create a list of letters from a-m a word 
def createListnzByWord(word,vowels = ['a','i','e','o','u']):
    return list([word[i]  for i in range(0,len(word)) if word[i].lower()<='z' and word[i].lower()>='n'and not word[i].lower() in vowels])

#method to create a dictionary
def createDic(keys,values,dic):
    if len(keys) == 0:
        return dic
    dic[keys[0]] = values[0]
    return  createDic(keys[1:],values[1:],dic)


#'פונקציות לסעיף ב
#
def treaTxtFile(flName,merge =[]):
    with open(flName,'r') as f:
        for line in f:
            merge.append(treatLine(checkAllLetters(line),line))
        f.close()
    return merge 

#  
def sikumofayim1(fldict,vals = []):
  vals = list(fldict.values())
  orgnizedList = list(zip(*[item for item in vals]))
  return [sum([len(orgnizedList[0][i]) for i in range(0,len(orgnizedList[0]))]),
         sum([len(orgnizedList[1][i]) for i in range(0,len(orgnizedList[1]))]),
          sum([len(orgnizedList[2][i]) for i in range(0,len(orgnizedList[2]))])]
     
#
def sumAll(fldict):
    if len(fldict) == 0:
        return[]
    return sumAll(fldict[:-1])+sikumofayim1(fldict[-1][1])

#
def sikumofayim(fldict):
    listSum = sumAll(fldict)
    return [sum([listSum[i] for i in range(0,len(listSum),3)]),
            sum([listSum[i] for i in range(1,len(listSum),3)]),
            sum([listSum[i] for i in range(2,len(listSum),3)]),
            sum([listSum[i] for i in range(0,len(listSum))])]

#
def createingOneTuple(l):
    if len(l) == 0:
        return []
    return createingOneTuple(l[:-1])+l[-1]
    

#
def printingAll(fldict):
  return  list([print(f"sentence: {list(fldict[i][1].keys())} LineNr:{fldict[i][0]} nr of vowels: {createingOneTuple(list(zip(*[item for item in list(fldict[i][1].values())]))[0])} nr of b-m consonants:{createingOneTuple(list(zip(*[item for item in list(fldict[i][1].values())]))[1])}nr of n-z consonants:{createingOneTuple(list(zip(*[item for item in list(fldict[i][1].values())]))[2])}") for i in range(0,len(fldict))])

#
def main():
    line = "This is an example"
    #print(treatLine(checkAllLetters(line),line))
    #print()
   # line1 = "t4his is an example"
   #print(treatLine(checkAllLetters(line1),line1))
    x = treaTxtFile("myDay.txt")
    #print(x)
    x.remove(x[-1])
    #print((sumAll(x[:-1])))
   #print(sikumofayim(x[:-1]))
    print(printingAll(x[:-1]))
    


main()
