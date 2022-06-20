class Solution:
    def average(self, salary: List[int]) -> float:
        sum, len = 0, 0
        min, max = salary[0], salary[0]
        
        for e in salary:
            if e < min:
                min = e
            elif e > max:
                max = e
                
            sum += e
            len += 1
            
        return (sum - max - min)/(len - 2)