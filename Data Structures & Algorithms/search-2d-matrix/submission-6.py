class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2 

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                #potentially found a candidate row 
                break
        
        if top > bottom:
            #if ptrs cross that means candidate row doesn't exist
            return False 

        candidate_row = (top + bottom) // 2

        #perform binary search on candidate row 

        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[candidate_row][mid] < target:
                left = mid + 1
            elif matrix[candidate_row][mid] > target:
                right = mid - 1
            else:
                return True
        
        return False 

