class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.findBound(nums, target, True)
        if lower == -1:
            return [-1, -1]
        upper = self.findBound(nums, target, False)
        
        return [lower, upper]
        
    def findBound(self, nums, target, isLeft):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot = left + (right - left)//2
            
            if nums[pivot] == target:
                if isLeft:
                    if left == pivot or nums[pivot - 1] < target:
                        return pivot
                    right = pivot - 1
                else:
                    if right == pivot or nums[pivot + 1] > target:
                        return pivot
                    left = pivot + 1                
                
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return -1
        