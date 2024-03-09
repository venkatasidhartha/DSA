#  Question 1 Missing Number

# formula
# 1+2+3+.....+n = n(n+1)/2
my_list = [1,3,4,5,6,7,8,9,10]
def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    
    return missing
# Example
print(missing_number(my_list, 10))