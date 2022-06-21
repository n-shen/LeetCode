class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 12321
        if x >= 0:
            digits = []
            while x > 0:
                digits.append(x%10)
                x //= 10

            size = len(digits)
            for i in range(size//2):
                if digits[i] != digits[size-i-1]:
                    return False
            return True
        else:
            return False
            
            