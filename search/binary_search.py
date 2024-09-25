import math


def binarySearch(array,value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value) and (start<=end):
        if value < array[middle]:
            end = middle -1
        else:
            start = middle +1
        middle = math.floor((start+end)/2)
        print(start,middle,end)
    if array[middle] == value:
        return middle
    else:
        return -1

a = [1,2,3,4,5,6,7,8,9,10,11]
print(binarySearch(a,15))
