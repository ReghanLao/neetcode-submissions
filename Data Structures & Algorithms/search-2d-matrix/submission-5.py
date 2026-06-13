class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # finding the target row 
        top = 0
        bottom = rows - 1

        # while the top and bottom row pts dont cross
        while top <= bottom:
            mid = (top + bottom) // 2

            # if our target is greater than the last element of 
            #current row that means our target is not in current row 
            #or any rows above 
            if target > matrix[mid][-1]:
                top = mid + 1
            # if our target is less than the first element of 
            #current row that means our target is not in current row
            #or any rows below
            elif target < matrix[mid][0]:
                bottom = mid - 1
            #we may have potentially found our target row
            else:
                break
            
        #there may be a chance we did not find target row which means
        #ptrs have crossed so no solution found
        if top > bottom:
            return False
        
        #else we have a valid row define by the top and bottom 
        #ex top could be 0 and bottom could be 0
        target_row = (top + bottom) // 2

        left = 0
        right = cols - 1

        #run binary search on this row to find the target 
        while left <= right:
            mid = (left + right) // 2

            if target < matrix[target_row][mid]:
                right = mid - 1
            elif target > matrix[target_row][mid]:
                left = mid + 1
            else:
                #we found the target element 
                return True
        
        #we did not find the target element in row
        return False


