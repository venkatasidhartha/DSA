"""
2D Lists
Given 2D list calculate the sum of diagonal elements.
"""

# my solution
def diagonal_sum(matrix):
    # TODO
    total = 0
    for index,elem in enumerate(matrix):
        total+=elem[index]
    return total
     
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
print(diagonal_sum(myList2D)) # 15

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


# SOLUTION - Time and Space Complexity of 2D Lists

def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
 
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
 
    return total

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""