class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        a, b = 0, 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                b += 1
            else:
                if b > a:
                    a = b
                b = 0
        
        return max(a + 1, b + 1)