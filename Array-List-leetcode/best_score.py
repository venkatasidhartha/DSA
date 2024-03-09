"""
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
"""

# My solution
def first_second(my_list):
    # TODO
    my_list.sort(reverse=True)
    return (my_list[0],my_list[1])

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList)) # 90 87
"""
Time Complexity: O(n log n)
Space Complexity: O(1)
"""


# SOLUTION - Time and Space Complexity of Best Score
def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
 
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
 
    return max1, max2
 
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
