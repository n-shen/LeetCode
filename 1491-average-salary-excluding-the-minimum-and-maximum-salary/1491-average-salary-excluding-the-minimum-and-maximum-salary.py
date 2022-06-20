class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        for e in salary:
            sum += e
            
        return (sum - max(salary) - min(salary))/(len(salary) - 2)