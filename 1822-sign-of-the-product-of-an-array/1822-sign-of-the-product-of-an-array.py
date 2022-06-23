class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        
        if 0 in nums:
            return 0
        
        for e in nums:
            if e < 0:
                product *= -1
                
        return product
    