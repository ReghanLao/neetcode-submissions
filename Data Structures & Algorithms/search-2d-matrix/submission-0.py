class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        flattened = []

        #go through every single row and flatten into new 1d arr
        for i in range(m):
            for j in range(n):
                flattened.append(matrix[i][j])
            
        
        left = 0
        right = len(flattened) - 1

        while left <= right:
            mid = (left + right) // 2

            if flattened[mid] == target:
                return True
            elif flattened[mid] > target:
                right = mid - 1
            elif flattened[mid] < target:
                left = mid + 1
        
        return False
