# Question - what is the runtime of the below code?

def printUnorderedPairs(array):
    for i in range(0,len(array)): # O(n)
        for j in range(i+1,len(array)): # O(n)
            print(array[i],array[j]) # O(1)


"""
Time Complexity: O(n^2)
"""

def printUnorderedPairs(arrayA,arrayB):
    for i in range(len(arrayA)): # O(a)
        for j in range(len(arrayB)): #O(b) -> here we have a different array this loop depend on this array
            if arrayA[i] < arrayB[j]: # O(1)
                print(arrayA[i],arrayB[j]) # O(1)

"""
a = len(arrayA)
b = len(arrayB)
Time Complexity: O(ab)
"""

def printUnorderedPairs(arrayA,arrayB):
    for i in range(len(arrayA)): # O(a)
        for j in range(len(arrayB)): # O(b)
            for k in range(0,1000000): # O(1) this is a constant loop 
                print(arrayA[i],arrayB[j]) # O(1)

"""
a = len(arrayA)
b = len(arrayB)
1000000 units of work is still constant 
Time Complexity: O(ab)
"""