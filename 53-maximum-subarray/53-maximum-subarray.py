class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        
        for e in nums[1:]:
            curSum = max(e, curSum + e)
            maxSum = max(maxSum, curSum)
        
        return maxSum