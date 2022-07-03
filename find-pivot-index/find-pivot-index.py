class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tSum = sum(nums)
        
        lSum = 0
        for i in range(len(nums)):
            if i > 0:
                lSum += nums[i - 1]
            
            if lSum*2 + nums[i] == tSum:
                return i
        return -1