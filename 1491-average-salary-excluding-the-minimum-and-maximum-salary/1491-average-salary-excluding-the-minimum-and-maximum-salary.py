class Solution:
    def average(self, salary: List[int]) -> float:
        min = salary[0]
        max = salary[1]
        sum = 0
        for i in range(len(salary)):
            if salary[i] < min:
                min = salary[i]
            if salary[i] > max:
                max = salary[i]
            
            sum += salary[i]
        
        return (sum - min - max)/(len(salary) - 2)