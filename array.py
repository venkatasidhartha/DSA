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