class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum0, sum1 = 0, 0
        for e in nums:
            sum0 += e
        
        for i in range(len(nums)):
            if i > 0:
                sum1 += nums[i - 1]
            
            if sum1*2 + nums[i] == sum0:
                return i
        return -1