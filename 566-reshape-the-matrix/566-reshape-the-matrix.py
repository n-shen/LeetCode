class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oneArr, newArr = [], []
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                oneArr.append(mat[i][j])
        
        if len(oneArr) != r*c:
            return mat
        else:
            for i in range(r):
                newArr.append([])
                for j in range(c):
                    newArr[i].append(oneArr[i*c + j]) 
        # print(oneArr)
        return newArr