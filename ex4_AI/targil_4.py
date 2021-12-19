# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:33:58 2020

@author:   צור איתן ומאור סרוסי
"""

from sklearn import tree

from sklearn.model_selection import cross_val_score

import matplotlib.pyplot as plt

from sklearn import datasets

# import some data to play with

iris = datasets.load_iris()

mylist = []
# do loop

clf = tree.DecisionTreeClassifier()

# clf.max_depth = 5

clf.criterion = 'entropy'

clf = clf.fit(iris.data, iris.target)

# print("Decision Tree: ")
# accuracy = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)


# print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(accuracy.mean(),3))


# precision = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)

# print("Average precision_weighted of  DT with depth ", clf.max_depth, " is: ", round(precision.mean(),3))

# f1score = cross_val_score(clf, iris.data, iris.target, scoring='f1_weighted', cv=10)

# print("Average f1 score of  DT with depth ", clf.max_depth, " is: ", round(f1score.mean(),3))

# recall = cross_val_score(clf, iris.data, iris.target, scoring='recall_weighted', cv=10)

# print("Average recall of  DT with depth ", clf.max_depth, " is: ", round(recall.mean(),3))

# X = range(10)
# plt.plot(X, [x*x  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# שאלה 2
# listByDepth = []
# myList = []

# for i in range(1,11):
#    clf.max_depth = i
#   accuracy = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
#  precision = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
# f1score = cross_val_score(clf, iris.data, iris.target, scoring='f1_weighted', cv=10)
# recall = cross_val_score(clf, iris.data, iris.target, scoring='recall_weighted', cv=10)
# macc = round(accuracy.mean(),3)
# mprecision = round(precision.mean(),3)
#  mf1score = round(f1score.mean(),3)
# mrecall = round(recall.mean(),3)
# listByDepth = [clf.max_depth,macc,mprecision,mf1score,mrecall]
# myList+=[listByDepth]

# print("    accuracy  precision  f1score  recall")
# for i in range(len(myList)):
# print("depth",myList[i][0],":",myList[i][1:])


# שאלה 3
# accList = []
# for i in range(1,11):
#   clf.max_depth = i
#   accuracy = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
#  accList.append(accuracy.mean()) # loop, can be used to plot later…
# X = range(1,11)
# plt.plot(X, [accList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# preList = []
# for i in range(1,11):
#  clf.max_depth = i
# precision = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
# preList.append(precision.mean()) # loop, can be used to plot later…

# X = range(1,11)
# plt.plot(X, [preList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# f1ScoreList = []
# for i in range(1,11):
#    clf.max_depth = i
#   f1Score = cross_val_score(clf, iris.data, iris.target, scoring='f1_weighted', cv=10)
#  f1ScoreList.append(f1Score.mean()) # loop, can be used to plot later…

# X = range(1,11)
# plt.plot(X, [f1ScoreList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

recallList = []
for i in range(1, 11):
    clf.max_depth = i
    recall = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
    recallList.append(recall)
print(recallList)
# recallList.append(recall.mean()) # loop, can be used to plot later…
# X = range(1,11)
# plt.plot(X, [recallList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# שאלה 4
# wine = datasets.load_wine()
# clf = clf.fit(wine.data, wine.target)

# accList = []
# for i in range(1,11):
#  clf.max_depth = i
# accuracy = cross_val_score(clf, wine.data, wine.target, scoring='accuracy', cv=10)
# accList.append(accuracy.mean()) # loop, can be used to plot later…
# X = range(1,11)
# plt.plot(X, [accList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()


# preList = []
# for i in range(1,11):
#  clf.max_depth = i
# precision = cross_val_score(clf, wine.data, wine.target, scoring='precision_weighted', cv=10)
# preList.append(precision.mean()) # loop, can be used to plot later…

# X = range(1,11)
# plt.plot(X, [preList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# f1ScoreList = []
# for i in range(1,11):
#   clf.max_depth = i
#  f1Score = cross_val_score(clf, wine.data, wine.target, scoring='f1_weighted', cv=10)
# f1ScoreList.append(f1Score.mean()) # loop, can be used to plot later…

# X = range(1,11)
# plt.plot(X, [f1ScoreList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# recallList = []
# for i in range(1,11):
#  clf.max_depth = i
#  recall = cross_val_score(clf, wine.data, wine.target, scoring='precision_weighted', cv=10)
#  recallList.append(recall.mean()) # loop, can be used to plot later…
# X = range(1,11)
# plt.plot(X, [recallList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# שאלה 5
# digits = datasets.load_digits()
# clf = clf.fit(digits.data, digits.target)

# accList = []
# for i in range(1,11):
#   clf.max_depth = i
#   accuracy = cross_val_score(clf, digits.data, digits.target, scoring='accuracy', cv=10)
#   accList.append(accuracy.mean()) # loop, can be used to plot later…
# X = range(1,11)
# plt.plot(X, [accList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# preList = []
# for i in range(1,11):
#   clf.max_depth = i
#  precision = cross_val_score(clf, digits.data, digits.target, scoring='precision_weighted', cv=10)
# preList.append(precision.mean()) # loop, can be used to plot later…

# X = range(1,11)
# plt.plot(X, [preList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# f1ScoreList = []
# for i in range(1,11):
#   clf.max_depth = i
#  f1Score = cross_val_score(clf, wine.data, wine.target, scoring='f1_weighted', cv=10)
# f1ScoreList.append(f1Score.mean()) # loop, can be used to plot later…

# X = range(1,11)
# plt.plot(X, [f1ScoreList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# recallList = []
# for i in range(1,11):
#  clf.max_depth = i
# recall = cross_val_score(clf, digits.data, digits.target, scoring='precision_weighted', cv=10)
# recallList.append(recall.mean()) # loop, can be used to plot later…
# X = range(1,11)
# plt.plot(X, [recallList[x-1]  for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()

# שאלה 6

iris = datasets.load_iris()
clf = tree.DecisionTreeClassifier()
clf.criterion = 'entropy'
clf = clf.fit(iris.data, iris.target)

wine = datasets.load_wine()
clf1 = tree.DecisionTreeClassifier()
clf1.criterion = 'entropy'
clf1 = clf1.fit(wine.data, wine.target)

digits = datasets.load_digits()
clf2 = tree.DecisionTreeClassifier()
clf2.criterion = 'entropy'
clf2 = clf2.fit(digits.data, digits.target)

accIrisList = []
accWineList = []
accDigitsList = []
for i in range(1, 11):
    clf.max_depth = i
    clf1.max_depth = i
    clf2.max_depth = i
    accIris = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
    accWine = cross_val_score(clf, wine.data, wine.target, scoring='accuracy', cv=10)
    accDigits = cross_val_score(clf, digits.data, digits.target, scoring='accuracy', cv=10)
    accIrisList.append(accIris.mean())
    accWineList.append(accWine.mean())
    accDigitsList.append(accDigits.mean())

maxIris = [max(accIrisList)]
maxWine = [max(accWineList)]
maxDigits = [max(accDigitsList)]
for i in range(10):
    if maxIris[0] == accIrisList[i]:
        maxIris.append(i + 1)
    if maxWine[0] == accWineList[i]:
        maxWine.append(i + 1)
    if maxDigits[0] == accDigitsList[i]:
        maxDigits.append(i + 1)

print("the max average for iris accuracy stock is", maxIris[0], "and it is found in depth:", maxIris[1:])

print("the max average for wine accuracy stock is", maxWine[0], "and it is found in depth:", maxWine[1:])

print("the max average for digits accuracy stock is", maxDigits[0], "and it is found in depth:", maxDigits[1:])
