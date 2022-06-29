class Solution:
    
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end - 1:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nLen = len(nums)
        k %= nLen
        
        self.reverse(nums, 0, nLen)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, nLen)