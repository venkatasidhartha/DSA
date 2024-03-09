# Question - what is the runtime of the below code?

def printPairs(array):
    for i in array: # O(n)
        for j in array: # O(n)
            print(i,j) # O(1)



"""
Time Complexity: O(n^2)
"""