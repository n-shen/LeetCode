class Solution:
    def firstUniqChar(self, s: str) -> int:
        sl = list(s)
        hm = {}
        
        for e in sl:
            if e in hm:
                hm[e] += 1
            else:
                hm[e] = 1
        
        for e in hm:
            if hm[e] == 1:
                return s.index(e)
        return -1
    