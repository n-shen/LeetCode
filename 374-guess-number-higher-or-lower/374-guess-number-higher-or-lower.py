# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1
        while left <= n:
            pivot = (left + n)//2
            
            if guess(pivot) == 0:
                return pivot
            elif guess(pivot) < 0:
                n = pivot - 1
            else:
                left = pivot + 1