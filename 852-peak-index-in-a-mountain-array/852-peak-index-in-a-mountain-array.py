class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        
        while left <= right:
            pivot = (left+right)//2
            
            if arr[pivot] < arr[pivot + 1]:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return left