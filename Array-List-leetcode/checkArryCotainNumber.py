# Question3 - How to check if an array contains a number in python 

import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10])

def find_number(arrray,number):
    for i in range(len(arrray)):
        if arrray[i] == number:
            print(i)

find_number(myArray,5)