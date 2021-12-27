#
# Targil 4  
#
# Use the following input lists:
#
from statistics import mean
from statistics import stdev

jctMarks = [[12345, 75, 'English'],
            [23452, 83, 'Physics'],
            [23560, 81, 'Statistics'],
            [23415, 61, 'Computer'],
            [23459, 90, 'Physics'],
            [12345, 75, 'Computer'],
            [23452, 100, 'Statistics']]

teacherName = [['Aharoni', 'English'],
               ['Melamed', 'Physics'],
               ['Kaner', 'Computer'],
               ['Zloti', 'Statistics'],
               ['Korman', 'Philosophy'],
               ]


#

# list
# method for get all teachers that had a students
def listsOfStu1(L, L1):
    """
    a function to get pair from 2 lists
    :param L: the 1st list
    :param L1: the 2nd list
    :return: a list of lists by the condition
    """
    return [[L1[i][0], [L[j][0]]] for i in range(0, len(L1)) for j in range(0, len(L)) if L1[i][1] == L[j][2]]


# method for get teachers without any student
def listsOfStu2(L, L1):
    """
    a function to get pair from 2 lists
    :param L: the 1st list
    :param L1: the 2nd list
    :return: a list of lists by the condition
    """
    return [[L1[i][0], []] for i in range(0, len(L1)) if not L1[i][1] in L]


# method for get all subject by students
def listOfSubjects(L):
    """
    a function to get pair from 2 lists
    :param L: the 1st list
    :param L1: the 2nd list
    :return: a list of terms
    """
    return [L[i][2] for i in range(0, len(L))]


# method to union all teachers with the students who learn with him
def unionByTeacher(l):
    """
    a function to union teachers by their students
    :param l:the list of teachers
    :return: the union
    """
    if len(l) == 0:
        return []
    if l[0][0] == l[1][0]:
        l[0][1].append(l[1][1][0])
        l.remove(l[1])
    return unionByTeacher(l[1:]) + [l[0]]


# method for get all students grades and put them in the teacher who learn them
def StudentsGradesByTeachers(L, L1):
    """
    a function to return the grades of students by their teachers
    :param L: the list with the student details
    :param L1: the list with the teacher details
    :return: a list with grades by teacher
    """
    return [[L1[i][0], [L[j][1]]] for i in range(0, len(L1)) for j in range(0, len(L)) if L1[i][1] == L[j][2]]


# method to get the average of students grade by teacher
def avgByTeacher(L, L1):
    """
    a function to get the avg by teacher
    :param L: the teacher list with his students
    :param L1: the teacher list with the grades
    :return: the avg of teacher
    """
    if len(L) == 0:
        return []
    L[0].insert(2, [mean(L1[0][1])])
    return avgByTeacher(L[1:], L1[1:]) + [L[0]]


# method to get stddev students grade by their teacher
def stddevByTeacher(L, L1):
    """
    a function to get stddev student grades by their teachers
    :param L: the list of the teachers by students and avg grades
    :param L1: the list of the teachers and the grades
    :return: the 1st list with the addition of stddev
    """
    if len(L) == 1:
        L[0][2].insert(1, stdev(L1[-1][1]))
        return [L[0]]
    if len(L1[-1][1]) > 1:
        L[0][2].insert(1, stdev(L1[-1][1]))
    else:
        L[0][2].insert(1, 0.0)
    return stddevByTeacher(L[1:], L1[:-1]) + [L[0]]


# method to get the overall average and stddev grades
def overallStddevAvg(L):
    """
    a function to get the overall avg and stddev grades
    :param L: the list of the students
    :return: a list with the overall stddev and avg
    """
    avg = [L[i][1] for i in range(0, len(L))]
    stDev = stdev(avg)
    return ["overall avg: " + str(mean(avg)) + ", overall stddev: " + str(stDev)]


#
def myStuList(L, L1):
    """
    a function to get for every teacher his students and their avg + stddev
    :param L: the students
    :param L1: the teacher
    :return:  a list with all the details
    """
    return (stddevByTeacher(
        avgByTeacher(unionByTeacher(listsOfStu1(L, L1)), unionByTeacher(StudentsGradesByTeachers(L, L1))),
        unionByTeacher(StudentsGradesByTeachers(L, L1))) +
            listsOfStu2(listOfSubjects(L), L1) + overallStddevAvg(L))


# dictionary

# general method to create dictionary
def myStuDict(L):
    """
    a function to create a dictionary
    :param L: the list we use
    :return: a dictionary
    """
    return dict(zip(teachers(L), values(L)))


# method to create teachers' list
def teachers(L):
    """
    a function to create the teachers' list
    :param L: the list with the details
    :return: a list with the teachers
    """
    return [L[i][0] for i in range(0, len(L) - 1)]


# method to create Values' list
def values(L):
    """
    a function to create values' list
    :param L: the list with the details
    :return:  the values' list
    """
    return [[L[i][1], tuple(L[i][2])] for i in range(0, len(L) - 1) if len(L[i]) == 3]


# method to print dictionary and overall details(average and stddev)
def printForMain(d, L):
    """
    a helper function for printing
    :param d: the dictionary
    :param L: the list with the teachers' details
    :return:
    """
    if len(L) == 1:
        print(L[0])
        return
    if not len(L[0][1]) == 0:
        print(str(L[0][0]), ":", "id's,grades' average and stddev", str(d[L[0][0]]))
    else:
        print(str(L[0][0]), ":", "[]")
    return printForMain(d, L[1:])


#
def main():
    unionGrades = unionByTeacher(StudentsGradesByTeachers(jctMarks, teacherName))
    subjects = listOfSubjects(jctMarks)
    unionIds = unionByTeacher(listsOfStu1(jctMarks, teacherName))
    NoStu = listsOfStu2(subjects, teacherName)
    averages = avgByTeacher(unionIds, unionGrades)
    stDev = stddevByTeacher(averages, unionGrades)
    overall = overallStddevAvg(jctMarks)
    allList = stDev + NoStu + overall
    L = (myStuList(jctMarks, teacherName))
    d = (myStuDict(L))
    printForMain(d, L)


main()
