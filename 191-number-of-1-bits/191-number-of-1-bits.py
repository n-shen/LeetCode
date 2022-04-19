class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        bstr = '{:032b}'.format(n)
        for b in bstr:
            if int(b): result += 1
        
        return result