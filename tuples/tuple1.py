# what is tuple?
"""
a tuple is an immutable sequence of python objects
tuples are also comparable and hashable

comparable - sortable
hashable - can use is as a key value pair

syntex : (1,2)
"""

newTuple = 1,2,3,4
print(newTuple)
"""
output 
(1, 2, 3, 4)
"""

newTuple = (1,2,3,4)
print(newTuple)
"""
output 
(1, 2, 3, 4)
"""

newTuple = tuple('1234')
print(newTuple)
"""
output 
(1, 2, 3, 4)
"""

"""
Time Complexity:O(1)
space Complexity:O(n)
"""

# tuple in memory / accessing an element of tuple

tuble1 = (1,2,3,2,4,5)
print(tuble1[2])
print(tuble1[:3])


# iterate a tuple
for i in tuble1:
    print(i)
"""
accessing tuple is almost like list
"""

"""
Time Complexity:O(n)
space Complexity:O(1)
"""


#  searching element in tuple

print(2 in tuble1) # O(n)
print(2 not in tuble1) # O(n)

print(tuble1.index(2)) # O(n)

"""
we can search element using linear search concept  like list
"""


# tuple opertaion / functions

mytuple = (1,2,3,4,5)
mytuple1 = (1,2,3,4,5,6,7)
print(mytuple + mytuple1) # merging two tuple plus operatot
"""
output
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7)
"""
print(mytuple*2) # if we use * operator it will repet the element as per we mention as intiger in right side ex: (1,2) * 2 = (1,2,1,2)
"""
output 
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
"""

print(mytuple1.count(2)) # this will return the count of the element that present in the tuple 


"""
Operation                               Time Complecity     Space Complecity

creating an tuple                           O(1)                O(N)
traversing a tuple                          O(N)                O(1)
accessing a cell                            O(1)                O(1)
searching a value                           O(N)                O(1)
"""