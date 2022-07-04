class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNumId = 0
        secondMaxNumId = -1
        
        n = len(nums)
        if n == 1:
            return 0
        
        for i in range(n):
            if nums[i] > nums[maxNumId]:
                secondMaxNumId = maxNumId
                maxNumId = i
            elif (secondMaxNumId < 0 or nums[i] > nums[secondMaxNumId]) and i != maxNumId:
                secondMaxNumId = i
        
        if nums[maxNumId] >= nums[secondMaxNumId]*2:
            return maxNumId
        else:
            return -1
                