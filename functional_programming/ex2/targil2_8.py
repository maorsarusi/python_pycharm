#
def add3dicts(d1,d2,d3):
    d = dictCreate(d1,d2)
    dictAll =dictCreate(d,d3)
    return dictAll
#
def mergeValue(key1,key2):
      l1 = set(key1)
      l2 = set(key2)
      l1Merge = list(filter(lambda i : i in l1 and not i in l2,l1))
      l2Merge = list(filter(lambda i : i in l2 and not i in l1,l2))
      lValues =l1Merge +l2Merge
      return tuple(lValues)
#
#
def findIntersectionKeys(d1,d2):
    s = set(d1).intersection(set(d2))
    return list(s)

#
def findNoneIntersectionKeys(d1,d2):
        s1= set(d1)
        s2 = set(d2)
        l1 = list(filter(lambda i : i  in s1 and not i in s2,s1))
        l2 =  list(filter(lambda i : i  in s2 and not i in s1,s2))
        return (l1+l2)

#
def returnValue(d1,d2,i,l):
    if l[i] in d1 and l[i] in d2:
         return mergeValue(d1[l[i]],d2[l[i]])
    elif l[i] in d2:
        return d2[l[i]]
    elif l[i] in d1:
        return d1[l[i]]
  
#
def dictCreate(d,d1):
    l = findNoneIntersectionKeys(d,d1)
    l1 = findIntersectionKeys(d,d1)
    lKeys = sorted(l1+l)
    lValues =list(map(lambda i: returnValue(d,d1,i,lKeys),range(len(lKeys))))
    return dict(zip(lKeys,lValues))


#תוכנית ראשית
if __name__ == "__main__":
   d1 = dict([(1,'a'),(3,'d'),(5,'e')])
   d2 = dict([(1,'b'), (3,(11,22)), (7,'f'), (4,'q')])
   d3 = dict([(2,'c'), (3,'x'), (4,'t'), (8,'g')])
   print("your one dictionary made by combined 3 dictionaries is: ")
   print(add3dicts(d1,d2,d3))
