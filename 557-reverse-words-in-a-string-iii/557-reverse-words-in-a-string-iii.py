class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split()
        result = ""
        
        for e in strList:
            wordList = list(e)
            start, end = 0, len(e) - 1
            while start < end:
                wordList[start], wordList[end] = wordList[end], wordList[start]
                start, end = start + 1, end - 1
            
            space = ""
            result += space.join(wordList) + ' '
        
        return result[:-1]
        