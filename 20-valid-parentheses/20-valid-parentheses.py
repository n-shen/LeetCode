class Solution:
    def isValid(self, s: str) -> bool:
        left_par = ['(', '[', '{']
        strStack = []
        for e in s:
            if e in left_par:
                strStack.append(e)
            elif len(strStack) > 0:
                top = strStack.pop()
                if (top == '(' and e != ')') or (top == '[' and e != ']') or (top == '{' and e != '}'):
                    return False
            else:
                return False
                
        return strStack == []