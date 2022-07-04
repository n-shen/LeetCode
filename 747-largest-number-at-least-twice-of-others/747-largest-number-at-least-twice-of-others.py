class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2, index = None, None, -1
        
        n = len(nums)
        if n == 1: return 0
        
        for i in range(n):
            if max1 == None or nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                index = i
            elif max2 == None or nums[i] > max2:
                max2 = nums[i]
                
        return index if max1 >= max2*2 else -1