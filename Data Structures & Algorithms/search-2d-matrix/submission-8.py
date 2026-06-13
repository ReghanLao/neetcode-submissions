class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first find the target row that the target could exist in 
        top = 0 
        bottom = len(matrix) - 1

        #keep shifting row boundaries til we converge onto one single row
        while top < bottom:
            mid = (top + bottom) // 2
            
            #if the first element of the given row is greater than 
            #our target then the target cannot be in this row or any subsequent rows
            if matrix[mid][0] > target:
                bottom = mid - 1
            #if the last element of a given row is less than 
            #our target then the target cannot in this row or previous rows
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
            #if the first element is less than our target and 
            #if our last element is greater than our target this is the target row\
                top = mid 
                bottom = mid  
                break 
        
        #if the pointers cross well then we don't have a valid row to search 
        #meaning the target is not in any of the rows 
        if top > bottom or bottom > top:
            return False

        #found target row so now perform regular binary search on this row
        target_row = top

        left = 0 
        right = len(matrix[target_row]) - 1

        #if we are able to find target return true else return false at the end of our search 
        while left <= right:
            mid = (left + right) // 2

            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                right = mid - 1
            elif matrix[target_row][mid] < target: 
                left = mid + 1
        
        return False
