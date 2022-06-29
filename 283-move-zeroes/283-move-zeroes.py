class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt1, pt2 = 0, 0
        n = len(nums)
        
        while pt2 < n:
            if nums[pt1] == 0:
                while pt2 < n and nums[pt2] == 0:
                    pt2 += 1
                if pt2 < n:
                    nums[pt1] = nums[pt2]
                    nums[pt2] = 0
            
            pt1 += 1
            pt2 += 1
                