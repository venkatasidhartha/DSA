# Question 6 -Permutation

def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    return list1 == list2

list1 = ['a','b','c']
list2 = ['c','b','a']
print(permutation(list1,list2))

"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""