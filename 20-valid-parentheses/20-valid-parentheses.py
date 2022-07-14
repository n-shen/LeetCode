class Solution:
    def isValid(self, s: str) -> bool:
        left_par = ['(', '[', '{']
        right_par = [')', ']', '}']
        strStack = []
        for e in s:
            if e in left_par:
                strStack.append(e)
            elif strStack:
                top = strStack.pop()
                if e != right_par[left_par.index(top)]:
                    return False
            else:
                return False
                
        return strStack == []