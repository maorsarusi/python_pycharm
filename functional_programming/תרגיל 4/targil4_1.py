#
# Targil 4  
#
# Use the following input lists:
#
from statistics import mean
from statistics import stdev

jctMarks = [[12345,75,'English'],
             [23452,83,'Physics'],
             [23560,81,'Statistics'],
             [23415,61,'Computer'],
             [23459,90,'Physics'],    
             [12345,75,'Computer'],
             [23452,100,'Statistics']]

teacherName = [['Aharoni','English'],
               ['Melamed','Physics'],
               ['Kaner','Computer'],
               ['Zloti','Statistics'],
               ['Korman','Philosophy'],
               ]

#

#list
#method for get all teachers that had a students
def listsOfStu1(L,L1):
    return [[L1[i][0],[L[j][0]]] for i in range(0, len(L1)) for j in range(0,len(L)) if L1[i][1] == L[j][2]]

#method for get teachers witout any student
def listsOfStu2(L,L1):
    return [[L1[i][0],[]] for i in range(0,len(L1)) if not  L1[i][1] in L]

#method for get all subject by students
def listOfSubjects(L):
    return[L[i][2] for i in range(0,len(L))]

#method to union all teachers with the students who learn with him
def unionByTeacher(l):
    if len(l) == 0 :
        return []
    if l[0][0] == l[1][0]:       
        l[0][1]. append(l[1][1][0])
        l.remove(l[1])
    return unionByTeacher(l[1:])+[l[0]]

#method for get all students grades and put them in the teacher who learn them
def StudendsGradesByTeachers(L,L1):
    return [[L1[i][0],[L[j][1]]] for i in range(0, len(L1)) for j in range(0,len(L)) if L1[i][1] == L[j][2]]

#method to get the avarage of students grade by teacher
def avgByTeacher(L,L1):
    if len (L) == 0:
        return []    
    L[0].insert(2,[mean(L1[0][1])])
    return avgByTeacher(L[1:],L1[1:])+[L[0]]

#method to get stdev students grade by their teacher
def stdevByTeacher(L,L1):
     if len (L) == 1:
        L[0][2].insert(1,stdev(L1[-1][1]))
        return [L[0]]
     if len(L1[-1][1]) > 1:
       L[0][2].insert(1,stdev(L1[-1][1]))
     else:
         L[0][2].insert(1,0.0)
     return stdevByTeacher(L[1:],L1[:-1])+[L[0]]

#method to get the averall avarage and stdev grades     
def overallStdevAvg(L):
     avg = [L[i][1] for i in range(0,len(L))]
     stDev=stdev(avg)
     return["overall avg: "+str(mean(avg))+ ", averall stdev: "+str(stDev)]
#
def myStuList(L,L1):
    return (stdevByTeacher(avgByTeacher(unionByTeacher(listsOfStu1(L,L1)), unionByTeacher(StudendsGradesByTeachers(L,L1))),unionByTeacher(StudendsGradesByTeachers(L,L1)))+
           listsOfStu2(listOfSubjects(L),L1)+overallStdevAvg(L))



#dictionary

#general method to create dictionary
def myStuDict(L):
    return dict(zip(teachers(L),values(L)))

#method to create teachers' list
def teachers(L):
    return [L[i][0] for i in range(0,len(L)-1)]

#method to create Values' list
def values(L):
    return [[L[i][1],tuple(L[i][2])] for i in range(0,len(L)-1) if len(L[i]) == 3]


#method to print dictionary and overall details(avarage and stedv)
def printForMain(d,L):
    if len(L) == 1:
        print(L[0])
        return
    if not len(L[0][1])== 0:
     print(str(L[0][0]),":","id's,grades' avarage and stdev",str(d[L[0][0]]))
    else:
       print(str(L[0][0]),":","[]")
    return printForMain(d,L[1:])
    


#
def main():
    unionGrades =unionByTeacher(StudendsGradesByTeachers(jctMarks,teacherName))
    subjects =listOfSubjects(jctMarks)
    unionIds = unionByTeacher(listsOfStu1(jctMarks,teacherName))
    NoStu = listsOfStu2(subjects,teacherName)
    avarages = avgByTeacher(unionIds, unionGrades)
    stDev = stdevByTeacher(avarages, unionGrades)
    overall = overallStdevAvg(jctMarks)
    allList = stDev +NoStu +overall
    L = (myStuList(jctMarks,teacherName))
    d = (myStuDict(L))
    printForMain(d,L)
    
    
    
main()
    
