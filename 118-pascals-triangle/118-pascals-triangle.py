class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return result
        
        for i in range(numRows - 2):
            prev = result[len(result) - 1]
            curr = [1]
            for j in range(len(prev) - 1):
                curr.append(prev[j] + prev[j + 1])
            curr.append(1)
            result.append(curr)
        
        return result
    