class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        minIndex, minDis = -1, -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                mDis = abs(x - points[i][0]) + abs(y - points[i][1])
                if minDis == -1 or mDis < minDis:
                    minDis = mDis
                    minIndex = i
        
        return minIndex
        
        
                
                