#!/bin/python3

def getmean(datalist):
    sum = 0
    i = 0
    while i < len(datalist):
        sum += datalist[i]
        i += 1
    mean = sum / len(datalist)
    return mean


datalist = [1,2,3,4,5,15]

average = getmean(datalist)

print(average)
