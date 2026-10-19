class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
            naive solution:
            m*n linear scan

            log(m*n) approach can be done utilizing sorted properties -
            BS

            If we narrow down what row the target could possibly be in then 
            we can perform a BS on the row giving us a worst case log(m*n)
            run time 
        '''

        #find potential target row first as once again target might not exist
        #find this in log m time where m is the number of rows
        top = 0 
        bottom = len(matrix) - 1

        cand = None

        #if the target is not between any of these rows return false
        while top <= bottom:
            mid = (top + bottom) // 2

            #check if target between this candidate row
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                cand = mid
                break
            #use point 2 - first int of every row greater than last int of prev
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
        
        if cand is None:
            return False
        
        #search cand row

        left = 0 
        right = len(matrix[cand]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[cand][mid] == target:
                return True 
            elif matrix[cand][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        #target not in cand row
        
        return False



