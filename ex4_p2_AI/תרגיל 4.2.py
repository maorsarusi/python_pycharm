# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:21:23 2020

@author: מאור סרוסי
"""

# הערה :יש לי בעיה בהרצה של כל הקבצים ביחד,דיברתי עם אבי והוא אמר שזה
# לא בעיה וצריך להריץ הכל בנפרד

import math
import csv


# building an object fo every line in the files
class distClass:
    vector = []  # the vector of the current point
    dist = -1  # distance of current point from test point
    tag = '-'  # tag of current point


# constant vars
MALE = 'M'
FEMALE = 'F'
COTERET = "new classification"

# list for k values
ksList = [1, 7, 19]

with open('mytrain.csv', 'r') as mtf:
    lines = csv.reader(mtf)
    myTrain = list(lines)

with open('mytest.csv', 'r') as mtstf:
    lines = csv.reader(mtstf)
    myTest = list(lines)


# method to calculate euqlidian distance
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += pow(num1 - num2, 2)
    return (math.sqrt(distance), "euclidean Distance ")


# method for calculate menhaten distance
def menhatenDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += abs(num1 - num2)
    return (distance, "menhaten Distance")


# method for calculate hamming distance
def hammingDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        if not num1 == num2:
            distance += 1
    return (distance, "hamming Distance")


# generic method for all distances methods
def genDistsnce(disFunc, instance1, instance2, length):
    return disFunc(instance1, instance2, length)


# method to return the new classification by a choosen k, list is the sorted list af the objects by the distance
# from the current vector in mytest to the vectors in mytrain
def calculteClassificationByNumOfK(k, List):
    # counter for checking classification
    male = 0
    female = 0
    for i in range(0, k):  # running from 0-k
        if List[i].tag == MALE:
            male += 1
        else:
            female += 1
    if male > female:
        return MALE
    else:
        return FEMALE


# method for enter the title of the new tagging
def newClassification(List):
    newList = List
    if not COTERET in List:  # checking if the COTERET is in the list of the title
        newList.append(COTERET)
    return newList


# method for calculating distance
def calculatDistance(List1, List2, disFunc,
                     j):  # list1 = mytest,list2 = mytrain,disFunc = the function that we get by it our distance
    newFileList = []
    for i in range(1, len(List2)):
        obj = distClass()  # one record's distance and tag
        obj.vector = List2[i][0:-1]  # the value of the vector in the object
        obj.dist, name = genDistsnce(disFunc, obj.vector, List1[j][0:-1], len(obj.vector))
        obj.tag = List2[i][-1]
        newFileList.append(obj)
    newFileList.sort(key=lambda x: x.dist)  # we sorting the list of objects fromthe smallest to the biggest distance
    return newFileList, name  # returning the new sorted list and the name of the distance method we used


# method to enter the new classification ew got to the file by enter it to the end of the correct list
def newGender(List, func, k):  # list = mytest,func = the function that we get by it our distance
    genderCount = 0
    newFileList = []
    newList = List
    for i in range(1, len(List)):
        newFileList, name = calculatDistance(newList, myTrain, func,
                                             i)  # we get the sorted list of objects from mytrain and the name of the distance function we used
        gender = calculteClassificationByNumOfK(k,
                                                newFileList)  # we gwt the new classification for the vector at mytest by using k objects from the sorted mytrain
        if gender == newList[i][-1]:  # checking if the new classification = old classification
            genderCount += 1
        if not len(newList[i]) == len(newList[0]):
            newList[i].append(gender)
    return newList, genderCount, name  # return mytest with the addition of the new classification,the number of the equals classification and the name of the function that we get by it our distance


def question1():
    # learning from my file to know the if the  Classification 
    with open('myFile.csv', 'r') as myfile2:
        lines = csv.reader(myfile2)
        dataWithHeader = list(lines)

    # open my file test  for checking the classification
    with open('myFile_test.csv', 'r') as f:
        linesMyFile = csv.reader(f)
        linesMyFileList = list(linesMyFile)

        linesMyFileList[0] = newClassification(linesMyFileList[0])  # try to enter COTERET to the file

    eucDistances1 = []
    eucDistances2 = []

    for i in range(1, len(dataWithHeader)):
        # find the distance from all vectors in myFile from the 2 vectors in myFile_test
        # הערה בגלל שאני יודע שיש לי 2 ווקטורים אני מתייחב אליהם בנפרד וזה נראה יותר טוב כעיקרון יש אפשרות
        # להכניס את כל האובייקטים לרשימה אחת ולחלק בכמות הווקטוקים וכך לדעת כמה ווקטורים שייכים לכל בדיקה

        obj1 = distClass()  # one record's distance and tag
        obj1.vector = dataWithHeader[i][0:-1]
        obj1.dist, name = genDistsnce(euclideanDistance, obj1.vector, linesMyFileList[1][0:-1], len(obj1.vector))
        obj1.tag = dataWithHeader[i][-1]
        eucDistances1.append(obj1)

        # create a list of object by the 2nd vector at
        obj2 = distClass()  # one record's distance and tag
        obj2.vector = dataWithHeader[i][0:-1]
        obj2.dist, name = genDistsnce(euclideanDistance, obj2.vector, linesMyFileList[2][0:-1], len(obj2.vector))
        obj2.tag = dataWithHeader[i][-1]
        eucDistances2.append(obj2)

    # sorting the lists of objects by the distance
    eucDistances1.sort(key=lambda x: x.dist)
    eucDistances2.sort(key=lambda x: x.dist)

    classFor1 = calculteClassificationByNumOfK(3, eucDistances1)
    classFor2 = calculteClassificationByNumOfK(3, eucDistances2)

    # check if the new classification gender dosen't written already in the file
    if not len(linesMyFileList[1]) == len(linesMyFileList[0]):
        linesMyFileList[1].append(classFor1)

    if not len(linesMyFileList[2]) == len(linesMyFileList[0]):
        linesMyFileList[2].append(classFor2)

    with open('myFile_test.csv ', 'w', newline='') as myCSVtest:
        writer = csv.writer(myCSVtest)
        writer.writerows(linesMyFileList)

    success = "question 1 succeeded"
    return success


# print(question1())


def question2_a(k, func,
                fileName):  # k = number for knn, func = the method we use to calculate the distance,fileName = the name of the file we create
    k1List = myTest
    genderCount = 0
    k1List[0] = newClassification(k1List[0])
    k1List, genderCount, name = newGender(k1List, func,
                                          k)  # getting the file with the new gender, the number of the equals classification and the name of the distance method

    with open(fileName, 'w', newline='') as q2af:
        writer1 = csv.writer(q2af)
        writer1.writerows(k1List)
    accuracy1 = ((genderCount) / len(k1List[1:])) * 100  # the number of the precent accuracy

    print("the accuracy between the old tags and new tags in myTest in k =", k, "in", name, "is", int(accuracy1), "%")
    return


# question2_a(ksList[0],euclideanDistance,'mytest1e.csv ')


def question2_b(k, func,
                fileName):  # k = number for knn, func = the method we use to calculate the distance,fileName = the name of the file we create

    k7List = myTest
    genderCountb = 0
    k7List[0] = newClassification(k7List[0])
    k7List, genderCountb, name = newGender(k7List, func,
                                           k)  # getting the file with the new gender, the number of the equals classification and the name of the distance method
    with open(fileName, 'w', newline='') as q2bf:
        writer7 = csv.writer(q2bf)
        writer7.writerows(k7List)
    accuracy7 = (genderCountb) / len(k7List[1:]) * 100  # the number of the precent accuracy

    print("the accuracy between the old tags and new tags in myTest in k =", k, "in", name, "is", int(accuracy7), "%")
    return


# question2_b(ksList[1],euclideanDistance,'mytest7e.csv ')

def question2_c(k, func,
                fileName):  # k = number for knn, func = the method we use to calculate the distance,fileName = the name of the file we create
    k19List = myTest
    genderCountc = 0
    k19List[0] = newClassification(k19List[0])
    k19List, genderCountc, name = newGender(k19List, func,
                                            k)  # getting the file with the new gender, the number of the equals classification and the name of the distance method
    with open(fileName, 'w', newline='') as q2cf:
        writer19 = csv.writer(q2cf)
        writer19.writerows(k19List)

    accuracy19 = (genderCountc) / len(k19List[1:]) * 100  # the number of the precent accuracy

    print("the accuracy between the old tags and new tags in myTest in k =", k, "in", name, "is", int(accuracy19), "%")
    return


# question2_c(ksList[2],euclideanDistance,'mytest19e.csv ')

def question2_d():
    acc1 = 0
    acc7 = 0
    acc19 = 0

    with open('mytest1e.csv ', 'r') as mtaf:
        lines1 = csv.reader(mtaf)
        kList1 = list(lines1)

    with open('mytest7e.csv ', 'r') as mtbf:
        lines7 = csv.reader(mtbf)
        k7List = list(lines7)
    with open('mytest19e.csv ', 'r') as mtcf:
        lines19 = csv.reader(mtcf)
        k19List = list(lines19)

    for i in range(1, len(k19List)):  # all the list's length are equals
        accMax = 0  # the number of the highest accuracy

        # counting the accuracy
        if kList1[i][-1] == kList1[i][-2]:
            acc1 += 1
        if k7List[i][-1] == k7List[i][-2]:
            acc7 += 1
        if k19List[i][-1] == k19List[i][-2]:
            acc19 += 1
    accList = [acc1, acc7, acc19]  # list of the accuracy
    accMax = [i for i in range(len(accList)) if accList[i] == max(
        accList)]  # list comperhension to the place on ksLists of the k that gives the highest accuracy
    printing = "the higest accuracy in euclidean distance is: " + str(
        max(accList)) + "%" + " " + "and it in k = " + str(ksList[accMax[0]])
    return printing


# print(question2_d())


# in all question 2_e we use the methid from question2_a-c because its the same procces just the parameters are different and the result
def question2_e1(k1, func, fileName1):
    question2_a(k1, func, fileName1)
    return


def question2_e7(k7, func, fileName7):
    question2_b(k7, func, fileName7)
    return


def question2_e19(k19, func, fileName19):
    question2_c(k19, func, fileName19)
    return


# question2_e1(ksList[0], menhatenDistance, 'mytest1m.csv ')
# question2_e7(ksList[1], menhatenDistance, 'mytest7m.csv ')
# question2_e19(ksList[2], menhatenDistance, 'mytest19m.csv ')


# in all question 2_f we use the methid from question2_a-c because its the same procces just the parameters are different and the result
def question2_f1(k1, func, fileName1):
    question2_a(k1, func, fileName1)
    return


def question2_f7(k7, func, fileName7):
    question2_a(k7, func, fileName7)
    return


def question2_f19(k19, func, fileName19):
    question2_a(k19, func, fileName19)
    return


# question2_f1(ksList[0], hammingDistance, 'mytest1h.csv ')
# question2_f7(ksList[1], hammingDistance, 'mytest7h.csv ')
# question2_f19(ksList[2], hammingDistance,'mytest19h.csv ')


def question2_g():
    acc1 = 0
    acc7 = 0
    acc19 = 0
    maxAcc = []
    with open('mytest1e.csv ', 'r') as f1:
        lines1 = csv.reader(f1)
        kList1g = list(lines1)

    with open('mytest7e.csv ', 'r') as f2:
        lines7 = csv.reader(f2)
        k7Listg = list(lines7)
    with open('mytest19e.csv ', 'r') as f3:
        lines19 = csv.reader(f3)
        k19Listg = list(lines19)

        # counting the accuracy
    for i in range(1, len(k19Listg)):  # all the list's length are equals
        accMax = []  # here its a list because we use in it to enter the list af the highest accuracy for all distance method
        if kList1g[i][-1] == kList1g[i][-2]:
            acc1 += 1
        if k7Listg[i][-1] == k7Listg[i][-2]:
            acc7 += 1
        if k19Listg[i][-1] == k19Listg[i][-2]:
            acc19 += 1
    accListe = [acc1, acc7, acc19]  # list of the accuracy
    maxAcc = [max(accListe)]  # the highest accuracy to euclidean distance

    # creating a  tuple of(k,accuracy,distance method) by the highest accuracy
    accMax = [(ksList[i], accListe[i], "euclidean distance") for i in range(len(accListe)) if
              accListe[i] == max(accListe)]

    acc1 = 0
    acc7 = 0
    acc19 = 0

    with open('mytest1m.csv ', 'r') as fm1:
        lines1 = csv.reader(fm1)
        kList1m = list(lines1)

    with open('mytest7m.csv ', 'r') as fm2:
        lines7 = csv.reader(fm2)
        k7Listm = list(lines7)
    with open('mytest19m.csv ', 'r') as fm3:
        lines19 = csv.reader(fm3)
        k19Listm = list(lines19)

        # counting the accuracy
    for i in range(1, len(k19Listm)):  # all the list's length are equals
        if kList1m[i][-1] == kList1m[i][-2]:
            acc1 += 1
        if k7Listm[i][-1] == k7Listm[i][-2]:
            acc7 += 1
        if k19Listm[i][-1] == k19Listm[i][-2]:
            acc19 += 1
    accListm = [acc1, acc7, acc19]  # list of the accuracy
    maxAcc += [max(accListm)]  # adding the highest accuracy to menhatten distance

    # creating a  tuple of(k,accuracy,distance method) by the highest accuracy
    accMax += [(ksList[i], accListm[i], "menhatten distance") for i in range(len(accListm)) if
               accListm[i] == max(accListm)]

    acc1 = 0
    acc7 = 0
    acc19 = 0

    with open('mytest1h.csv ', 'r') as fh1:
        lines1 = csv.reader(fh1)
        kList1h = list(lines1)

    with open('mytest7h.csv ', 'r') as fh2:
        lines7 = csv.reader(fh2)
        k7Listh = list(lines7)
    with open('mytest19h.csv ', 'r') as fh3:
        lines19 = csv.reader(fh3)
        k19Listh = list(lines19)

        # counting the accuracy
    for i in range(1, len(k19Listh)):  # all the list's length are equals
        if kList1h[i][-1] == kList1h[i][-2]:
            acc1 += 1
        if k7Listh[i][-1] == k7Listh[i][-2]:
            acc7 += 1
        if k19Listh[i][-1] == k19Listh[i][-2]:
            acc19 += 1
    accListh = [acc1, acc7, acc19]  # list of the accuracy
    maxAcc += [max(accListh)]  # adding the highest accuracy for hamming distance

    # creating a  tuple of(k,accuracy,distance method) by the highest accuracy
    accMax += [(ksList[i], accListh[i], "hamming distance") for i in range(len(accListh)) if
               accListh[i] == max(accListh)]

    maxAcc = max(maxAcc)  # the higest accuracy from all the accuracies

    # creating a list of the tuple with the highest accuracy
    printing = [accMax[i] for i in range(len(accMax)) if maxAcc == accMax[i][1]]
    return "the highest combination of accuracy and k is in k = " + str(printing[0][0]) + " in " + printing[0][
        2] + " and its " + str(printing[0][1]) + "%"

# print(question2_g())
