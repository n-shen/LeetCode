class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        
        if num == 1:
            return True
        
        while right - left > 1:
            pivot = (left + right)//2
            
            if pivot * pivot == num:
                return True
            
            if pivot * pivot < num:
                left = pivot
            else:
                right = pivot
        
        return False