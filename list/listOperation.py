


myList = [1,2,3,4,5,6,7]
myList.append(9) 
"""
    Time complexity: O(1)
    Space complexity: O(1)
"""

myList.insert(3,44) 
"""
    Time complexity: O(N)
    Space complexity: O(1)
"""


new_list = [56,65,76]
myList.extend(new_list) 
"""
    Time complexity: O(N)
    Space complexity: O(N)
"""

#----------------------------
#Slice
print(myList[0:-1])

#----------------------------
#Delete
myList.pop(1)
"""
    Time complexity: O(N)
    Space complexity: O(1)
"""
print(myList)


del myList[2:4]
"""
    Time complexity: O(N)
    Space complexity: O(1)
"""
myList.remove(76)
"""
    Time complexity: O(N)
    Space complexity: O(1)
"""

print(myList)


#--------------------------------------------------

#searching 

liost = [1,2,3,4,5,6]
target = 3
if target in liost:
    print(f"{target} is there")
else:
    print(f"{target} is not there")


# liner search
def liner_search(array,target):
    for i in array:  #O(N)
        if i == target: # O(1)
            return i # O(1)
    return -1
"""
    Time complexity: O(N)
    Space complexity: O(1)
"""

print(liner_search(liost,5))

#------------------------------------------

# Plus operator (+)

a = [1,2,3,4,5]
b = [6,7,8]
print(a+b)
#------------------------------------------------------
#  (*) Operator

a = [0]
a = a * 4
print(a)
# --------------------------------------------------
#  len() function

a = [0,1,2,3]
print(len(a))
# ---------------------------------------
# max() function
print(max(a)) # rutern the larger element in list
# min() function
print(min(a)) # rutern the smaller element in list
# sum() function
print(sum(a)) # add all the elements in list

# ------------------------------------------

# Problem

"""

total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count
print("Average: ",average)

"""

"""
above problem can be solved by one more method 
to reduce the time complexity
"""

"""
arr = []
while True:
    inp = input("Enter a number: ")
    if inp == 'done': break
    arr.append(float(inp))
print("Average: ",(sum(arr)/len(arr)))
"""
#------------------------------------------------

# String and lists

a = 'spam'
b = list(a)
print(b)

a = "split you bro"
print(a.split(" "))
print("".join(a))

# -----------------------------------------------------
# Avoid this mistake doing in list

a = [3,8,1,4,0,5]
a = a.sort()
print(a) # this will return None

# ----------------------------------------------
#  List vs Arrays

import numpy as np

myArray = np.array([1,2,3,4,5])
print(myArray/2)
"""
output 
[0.5 1.  1.5 2.  2.5]
array have same data type its easy to perform arthimits oprtation
"""


myList = [1,2,3,4,5]
# print(myList/2)
"""
output
Traceback (most recent call last):
  File "/home/sidhu/DSA/list/listOperation.py", line 162, in <module>
    print(myList/2)
TypeError: unsupported operand type(s) for /: 'list' and 'int'

list is dynamic datatype its hard to perform

"""

myArray = np.array([1,2,3,4,'a'])
print(myArray)
"""
output 
['1' '2' '3' '4' 'a']
if there is string datatype it will covert the whole array elements into string  
"""
myList = [1,2,3,4,5,'a']
print(myList)
"""
output 
[1,2,3,4,5,'a']
in list it wont change any datatype it will handle multiple datatypes  
"""
# ---------------------------------------------------------



"""
Operation                               Time Complecity     Space Complecity

creating an empty array                     O(1)                O(1)
creating an array with elements             O(n)                O(n)
inserting a column/row in an array          O(n)                O(1)
traversing a array                          O(n)                O(1)
accessing a cell                            O(1)                O(1)
searching a value                           O(n)                O(1)
deleting a column/row                       O(n)                O(1)


"""