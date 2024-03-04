import array

my_array = array.array('i') # -> O(1)
print(my_array)
my_array1 = array.array('i',[1,2,3,4]) # -> O(N)
print(my_array1)


import numpy as np

np_array = np.array([],dtype=int) # -> O(1)
print(np_array)
np_array1 = np.array([1,2,3,4]) # -> O(N)
print(np_array1)


"""
so here the space and time complexity is Big O(N)
when the input size increse the space and time is also incress
"""

#----------------------------------------------------------

# Insertion

print(my_array1)

my_array1.insert(0,6) #-> O(N) because the

"""
the above statement is taking O(N) 
beacuse the insertion of the eleent is in a specific index the values need to be rearanged 
so 
Time Complexity: O(N)
Space Complexity: O(1)
"""

print(my_array1)

#----------------------------------------------------------

# Array Traversal (iterating)

def traverseArray(array):
    for i in array: #-> O(N)
        print(i) # #-> O(1)
    """
    Time Complexity: O(N)
    Space Complexity: O(1) because we don't need any new space to dicplay the value
    """

traverseArray(my_array1)

#----------------------------------------------------------

# Access array element

def accessElement(array,index):
    if index >= len(array): # O(1)
        print("There is not any element in this array") # O(1)
    else: 
        print(array[index]) # O(1)

    """
    Time complexity: O(1)
    Space complexity: O(1)
    """

accessElement(my_array1,4)

#----------------------------------------------------------

# searching for an element

def linear_search(arr,target):
    for i in range(len(arr)): #-> O(N)
        if arr[i] == target: # O(1)
            return i # O(1)
    return -1 # O(1)
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

print("linear_search ",linear_search(my_array1,9))

#----------------------------------------------------------

# Deleting an Element from Array
my_array1.remove(2) # O(N)
print("Deleting ",my_array1)
"""
    Time complexity: O(N)
    Space complexity: O(1)
"""

#----------------------------------------------------------

# Time and Space complexity of One Dimentional Array

"""
Operation                           Time Complexity     Space Complexity   

creating Empty array                    O(1)                O(1)
creating an array with elements         O(N)                O(N)
inserting value in array                O(N)                O(1)
traversing array                        O(N)                O(1)
accessing array                         O(1)                O(1)
searching array                         O(N)                O(1)
deleting array                          O(N)                O(1)
"""