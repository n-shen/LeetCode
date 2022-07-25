class Solution:
    def firstUniqChar(self, s: str) -> int:
        sl = list(s)
        hm = {}
        
        for i in range(len(sl)):
            if sl[i] in hm:
                hm[sl[i]][0] += 1
            else:
                hm[sl[i]] = [1, i]
        
        for e in hm:
            if hm.get(e)[0] == 1:
                return hm.get(e)[1]
        return -1
    