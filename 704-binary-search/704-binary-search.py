class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot = (right + left)//2
            
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                right = pivot - 1
            if nums[pivot] < target:
                left = pivot + 1
                
        return -1