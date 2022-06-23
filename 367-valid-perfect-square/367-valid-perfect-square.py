class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        
        if num == 1:
            return True
        
        while left <= right:
            pivot = (left + right)//2
            
            if pivot * pivot == num:
                return True
            
            if pivot * pivot < num:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return False