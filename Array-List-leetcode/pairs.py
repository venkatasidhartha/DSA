"""
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.
"""

# my solution
def pair_sum(myList, sum):
    # TODO
    new_arr = []

    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if (myList[i]+myList[j]) == sum:
                new_arr.append(f"{myList[i]}+{myList[j]}")
    return new_arr


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

# SOLUTION - Time and Space Complexity of Pairs
def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result
 
arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""