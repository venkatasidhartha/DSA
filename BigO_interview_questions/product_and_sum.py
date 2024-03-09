# Question - what is the runtime of the below code?

def foo(array):
    sum = 0 # O(1)
    product = 1 # O(1)

    for i in array:# O(N)
        sum+=i # O(1)
    
    for i in array:# O(N)
        product*=i # O(1)
    
    print("Sum = "+sum+" Product = "+product) # O(1)

"""
Time Complexity: O(N)
"""

