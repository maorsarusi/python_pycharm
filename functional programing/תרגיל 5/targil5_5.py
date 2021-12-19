import random
peopleNames=("Bar","Rotem","Jenifer","Yarden","Bridgit","Nataly")
verbs=("sees","eats","sleep","sings")
adjectives=("tall","small","wide","red","delicious")
animateObjects=("flower","oranges","apples")
adverbs=("slowly","tommorow","soon","today")
inanimateObjects=(" chicken meat"," stone"," chair")
# peopleName->adverbs->verbs->adjectives->[animateObjects || inanimateObjects]
wordsList = [peopleNames,adverbs,verbs,adjectives,[animateObjects,inanimateObjects]]
#
def prtPoem(poem):
     return list(print(' '.join(line))  for line in poem)
    

def chooseWord(words):
    if isinstance(words,list):
        w = words[random.randrange(0,2)]
    else:
        w = words       
    return w[random.randrange(0,len(words))]    

def crPoem(N,shir =[]):
    if N ==0:
        return shir
    else:
        return crPoem(N-1,shir + [list(map(chooseWord,wordsList))])
    



def theHumblePoet(N):
    if isinstance(N,int) and N>0:
        prtPoem(crPoem(N))
    else:
        print("ERROR,must be a positive number")


def main():
    x = eval(input("enter the number of the line you want:\n"))
    theHumblePoet(x)


main()
