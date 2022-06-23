class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        
        while left <= right:
            pivot = (left + right)//2
            
            if pivot * pivot == x:
                return pivot
            
            if pivot * pivot > x:
                right = pivot - 1
            else:
                left = pivot + 1
        
        return left - 1