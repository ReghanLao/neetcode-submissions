class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
            This matrix is sorted from
            left to right and top to bottom

            1. Each row is sorted in non decreasing order
            2. The first integer of a row is greater than the 
            last integer of the previous 

            Use BS on this matrix given the properties to find 
            a solution in log(m * n) time

            Using property 2 we can first find the row the target is potentially in

            After we have located the correct row, we can search that row
            to find the target using property 1 if it exists 
        '''

        top = 0 
        bottom = len(matrix) - 1
        row = None 

        #finding a candidate row the target could be in 
        while top <= bottom:
            mid = (top + bottom) // 2
            #check if target is in the calculated middle row
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid 
                break 
            #target has to be in upper rows
            elif target <= matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
            #target has to be in bottom rows 
                top = mid + 1

        #if we never a potential candidate row the target is not in our 
        #matrix
        if row is not None:
            print('hit')
            left = 0
            right = len(matrix[row]) - 1
            
            while left <= right:
                mid = (left + right) // 2

                if matrix[row][mid] == target:
                    return True 
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return False 
        else:
            return False