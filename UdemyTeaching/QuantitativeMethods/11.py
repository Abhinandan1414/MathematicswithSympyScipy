'''
In a class
10 students score 1
30 students score 2
30 students score 3
20 students score 4
10 students score 5
What is the expected value for this distribution and plot the
relevant plots
'''
import matplotlib.pyplot as plt
import math

def freqProbability(frequencyParam):
    print(frequencyParam)
    retList = []
    totalFrequency = 0
    for i in range(len(frequencyParam)):
        totalFrequency += frequencyParam[i]
    for i in range(len(frequencyParam)):
        retList.append(frequencyParam[i]/totalFrequency)
    return retList

def expectedValue(testScore,returnedList):
    expValue = 0
    print(testScore)
    print(returnedList)
    for i in range(len(testScore)):
        expValue += testScore[i]*returnedList[i]
    return expValue

testScore = [1,2,3,4,5]
frequency = [10,30,30,20,10]

def mainMethod():
    returnedList = freqProbability(frequency)
    print('ExpectedValue ',expectedValue(testScore,returnedList))
    x_axis = list(set(testScore))
    plt.bar(x_axis, returnedList)
    plt.show()

mainMethod()