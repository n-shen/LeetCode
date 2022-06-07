# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            pivot = (left + right)//2
            if isBadVersion(pivot):
                if not isBadVersion(pivot - 1):
                    return pivot
                right = pivot - 1
            else:
                left = pivot + 1
                