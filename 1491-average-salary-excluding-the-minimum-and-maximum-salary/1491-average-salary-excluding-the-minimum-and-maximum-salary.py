class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        for i in salary:
            sum += i
        
        return (sum - min(salary) - max(salary))/(len(salary) - 2)