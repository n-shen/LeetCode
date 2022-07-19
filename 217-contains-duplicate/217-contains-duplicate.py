class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        
        for e in nums:
            if e in hm:
                return True
            else:
                hm[e] = 1
        
        return False