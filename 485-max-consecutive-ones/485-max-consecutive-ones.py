class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = curNum = 0
        
        for e in nums:
            if e == 1:
                curNum += 1
            else:
                if curNum > maxNum:
                    maxNum = curNum
                curNum = 0
        
        return max(maxNum, curNum)