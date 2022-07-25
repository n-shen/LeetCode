class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tank = list(magazine)
        hm = {}
        
        for e in tank:
            if e not in hm:
                hm[e] = 1
            else:
                hm[e] += 1
        
        rn = list(ransomNote)
        for e in rn:
            if e in hm and hm[e] > 0:
                hm[e] -= 1
            else:
                return False
        return True
    