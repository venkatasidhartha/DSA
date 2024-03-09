"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
"""
# my solution
def contains_duplicate(nums):
    # TODO
    setCheck = set()
    for i in nums:
        if i not in setCheck:
            setCheck.add(i)
        else:
            return True
    return False

print(contains_duplicate([1,2,3]))
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


# SOLUTION - Time and Space Complexity of Contains Duplicate
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
 
# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicate(nums))  # Output: True
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""