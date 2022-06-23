class Solution:
    
    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
        
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for e in nums:
            product *= e
        
        return self.signFunc(product)