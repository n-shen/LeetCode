class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n, i = len(nums), 0
        newNums = [0]*(n//2)
        if n == 1:
            return nums[0]
        else:        
            for i in range(len(newNums)):
                if i%2 == 0: 
                    newNums[i] = min(nums[2*i], nums[2*i+1])
                else:
                     newNums[i] = max(nums[2*i], nums[2*i+1])
            return self.minMaxGame(newNums)
        