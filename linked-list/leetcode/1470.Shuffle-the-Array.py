#  my solution

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # method 1
        # a = nums[0:n]
        # b = nums[n:]
        finail = []
        for i in range(n):
            finail.append(a[i])
            finail.append(b[i])
        # print(finail)

        # method 2
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        print(nums[:n], nums[n:])
        print(nums[::2])
        print(nums)




        


Solution().shuffle([2,5,1,3,4,7],3)