
# Question 2 - Find Pairs
# LeetCode 1 - Two sum 
def findPairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] ==  nums[j]:
                continue
            elif nums[i]+nums[j] == target:
                print(i,j)

mylist = [1,2,3,2,3,4,5,6]
# findPairs(mylist,6)


def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 26
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")