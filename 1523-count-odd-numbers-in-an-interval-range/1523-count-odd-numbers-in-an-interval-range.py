class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 == 1:
            low -= 1
        if high%2 == 1:
            high += 1
            
        return int((high - low)/2)