class Solution:
    def isValid(self, s: str) -> bool:
        strStack = []
        for e in s:
            if e == '(' or e == '{' or e == '[':
                strStack.append(e)
            elif len(strStack) > 0:
                top = strStack.pop()
                if (top == '(' and e != ')') or (top == '[' and e != ']') or (top == '{' and e != '}'):
                    return False
            else:
                return False
                
        return len(strStack) == 0