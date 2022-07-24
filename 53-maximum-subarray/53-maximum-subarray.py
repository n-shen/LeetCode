class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = curr_sum = nums[0]
        
        for i in range(1, len(nums)):
            curr_sum += nums[i]
            curr_sum = max(curr_sum, nums[i])
            curr_max = max(curr_max, curr_sum)
        
        return curr_max    
        