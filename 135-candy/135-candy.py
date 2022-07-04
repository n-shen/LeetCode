class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        nums = [1]*n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                nums[i] = nums[i - 1] + 1
        
        total = nums[n - 1]
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                nums[i] = max(nums[i], nums[i + 1] + 1)
            total += nums[i]
        
        return total
        
                