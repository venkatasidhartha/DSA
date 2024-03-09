"""
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
"""

# My solution
def remove_duplicates(arr):
    # TODO
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

# SOLUTION - Time and Space Complexity of Duplicate Number
def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""