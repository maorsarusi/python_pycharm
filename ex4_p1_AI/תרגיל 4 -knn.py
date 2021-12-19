# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:17:24 2020

@author: מאור סרוסי
"""
import math
import csv

# שאלה 1
point = [1, 0, 0, '?']
data1 = [1, 1, 1, 'M']
data2 = [1, 2, 0, 'F']


# שאלה 2
# print("The vector",data1[0:-1],"has tag",data1[-1])
# print("The vector",data2[0:-1],"has tag",data2[-1])

# ההדפסה
# The vector [1, 1, 1] has tag M
# The vector [1, 2, 0] has tag F

# שאלה 3
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += pow(num1 - num2, 2)
    return math.sqrt(distance)


# print("the  distance between data1 and data 2 by euclideanDistance is:",euclideanDistance(data1,data2,len(data1)-1))

# ההדפסה
# the   distance between data1 and data 2 by euclideanDistance is: 1.4142135623730951

# שאלה 4
with open('myFile.csv', 'r') as myCsvfile:
    lines = csv.reader(myCsvfile)
    dataWithHeader = list(lines)

# put data in dataset without header line
dataset = dataWithHeader[1:]


# print("the 1st myFile.csv is: ",dataset[0])
# print("the 2nd myFile.csv is: ",dataset[1])
# print("the  distance between the 1st myFile.csv and the 2nd myFile.csv by euclideanDistance is:",euclideanDistance(dataset[0],dataset[1],len(dataset[0])-1))

# ההדפסה
# a
# the 1st myFile.csv is:  ['0', '1', '2', 'F']
# the 2nd myFile.csv is:  ['1', '5', '6', 'F']


# b
# the   distance between the 1st myFile.csv and the 2nd myFile.csv by euclideanDistance is: 5.744562646538029

# שאלה 5
class distClass:
    dist = -1  # distance of current point from test point
    tag = '-'  # tag of current point


eucDistances = []  # list of distances, will hold objects of type distClass
point = dataset[0]
point[-1] = "?"
for i in range(1, len(dataset)):
    temp = dataset[i]
    label = temp[-1]
    d = euclideanDistance(point, temp, 3)
    # print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
    # print(" and the label is " + label)
    obj = distClass()  # one record's distance and tag
    obj.dist = d
    obj.tag = label
    eucDistances.append(obj)

# שאלה 6
eucDistances.sort(key=lambda x: x.dist)
# print()


# שאלה 7
dataset.remove(dataset[0])
for i in range(len(dataset)):
    dataset[i].append(euclideanDistance(point, dataset[i], len(point) - 1))
dataset.sort(key=lambda x: x[-1])
for i in range(len(dataset)):
    dataset[i].remove(dataset[i][-1])
for i in range(len(dataset)):
    print("The distances between " + str(point[0:-1]) + " and " + str(dataset[i][0:-1]) + " is " + str(
        eucDistances[i].dist))
    print(" and the label is " + str(eucDistances[i].tag))

# שאלה 8
point[-1] = eucDistances[0].tag
# print(point)

# שאלה 9
k = 3
countM = 0
countF = 0
for i in range(k):
    if eucDistances[i].tag == 'M':
        countM += 1
    else:
        countF += 1
if countF > countM:
    point[-1] = 'F'
else:
    point[-1] = 'M'
print(point)
