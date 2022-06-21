class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num1, num2 = x, 0
        while x > 0:
            num2 = num2*10 + x%10
            x //= 10

        return num1 == num2
            
            