class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num = 0
        
        for e in nums:
            ds = 0
            while e > 0:
                e //= 10
                ds += 1
            if ds%2 == 0:
                num += 1
        
        return num