

def buildArray(nums):
        n = len(nums)
        for i in range(0, len(nums)):
            nums[i]=nums[i]+(n*(nums[nums[i]]%n))

        for i in range(0, len(nums)):
            nums[i] = int(nums[i]/n)

        return nums

buildArray([0,2,1,5,3,4])