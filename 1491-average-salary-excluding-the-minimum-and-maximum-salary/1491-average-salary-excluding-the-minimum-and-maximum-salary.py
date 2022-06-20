class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        len = 0
        for e in salary:
            sum += e
            len += 1
            
        return (sum - max(salary) - min(salary))/(len - 2)