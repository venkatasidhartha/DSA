"Two Dimensional array"

# Day 1 - 11,15,10,6
# Day 2 - 17,14,67,89
# Day 3 - 55,67,89,12
# Day 4 - 23,43,56,12

import numpy as np

twoDArray = np.array([[11,15,10,6],[17,14,67,89],[55,67,89,12],[23,43,56,12]]) 
"""
    the above line complexity
    Time complexity: O(N)
    Space complexity: O(N)

    because it has N no of rows and N no of columns
"""
print(twoDArray)

# --------------------------------------------------------------------

# Insert Element in a specific index

newTwoDarray = np.insert(twoDArray,0,[1,2,3,4],axis=0) # axis = 1 it will add to column or axis = 0 it will add to row in a specific index
print("newTwoDarray",newTwoDarray)
"""
    the above line complexity (m - column N - row)
    Time complexity: O(mN) 
    Space complexity: O(mN)

    because it has N no of rows and N no of columns
"""

# --------------------------------------------------------------------

# Append the element at last of the array
 
newTwoDarray_aapend = np.append(twoDArray,[[1,2,3,4]],axis=0) # axis = 1 it will add to column or axis = 0
print("newTwoDarray_aapend",newTwoDarray_aapend)
"""
    the above line complexity (m - column N - row)
    Time complexity: O(mN) 
    Space complexity: O(mN)

    because it has N no of rows and N no of columns
"""

# --------------------------------------------------------------------

# Access elements in array

def accessElements(array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]): # O(1)
        print("Incorrect Index") # O(1)
    else: # O(1)
        print(array[rowIndex][colIndex]) # O(1)

accessElements(twoDArray,1,4)

"""
    the above line complexity
    Time complexity: O(1) 
    Space complexity: O(1)

    because accessing the element using index
"""

# --------------------------------------------------------------------

# Traversal (iterate)
def traverseTDarray(array):
    for row in range(len(array)): # O(mN)
        for col in range(len(array[0])):  # O(N)
            print(array[row][col]) # O(1)


traverseTDarray(twoDArray)
"""
    the above line complexity
    Time complexity: O(n^2) 
    Space complexity: O(1)

    because accessing each element
"""

# --------------------------------------------------------------------
# searching elements

def searchTDarray(array,value):
    for row in range(len(array)): # O(mN)
        for col in range(len(array[0])):  # O(N)
            if value == array[row][col]: # O(1)
                return f"The value is located at index row = {row} column = {col}"
    return 'The element is not found'

print(searchTDarray(twoDArray,43))

"""
    the above line complexity
    Time complexity: O(n^2) 
    Space complexity: O(1)

    because searching each element
"""

# --------------------------------------------------------------------
# Deletion 

newTDdeletearray = np.delete(twoDArray,0,axis=0) # axis = 1 it will delete to column or axis = 0 it will delete row in a specific index
print(newTDdeletearray)

"""
    the above line complexity
    Time complexity: O(n^2) 
    Space complexity: O(N)

    because Coping the data to new memory space incress time and space
"""

# --------------------------------------------------------------------

# Time and Space Complexity of 2D array

"""
 (m - column N - row)
Operation                               Time Complecity     Space Complecity

creating an empty array                     O(1)                O(1)
creating an array with elements             O(mN)               O(mN)
inserting a column/row in an array          O(mN)               O(mN)
traversing a array                          O(mN)               O(1)
accessing a cell                            O(1)                O(1)
searching a value                           O(mN)               O(1)
deleting a column/row                       O(mN)               O(mN)


"""