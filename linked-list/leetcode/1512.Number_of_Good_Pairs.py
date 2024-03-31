
# my solution with two for loop

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i < j:
                    count+=1
        return count








# AI Solution with one for loop 
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        count = 0
        num_counts = {}
        for num in nums:
            if num in num_counts:
                count += num_counts[num]
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        return count

print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
