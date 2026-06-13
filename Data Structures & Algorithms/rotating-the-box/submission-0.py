class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        #going row by row and sinking rocks to empty free spots 
        #two pointers (one going thru the row and one to indicate a free spot)

        def swap(row, i, j):
            temp = boxGrid[row][i]
            boxGrid[row][i] = boxGrid[row][j]
            boxGrid[row][j] = temp 

        num_rows = len(boxGrid)
        num_cols = len(boxGrid[0])

        #sinking of rocks to proper position 
        for row in range(num_rows):
            free_space = num_cols - 1
            for col in range(num_cols - 1, -1, -1):
                #if the current char is a stone we swap it to the next available free space
                if boxGrid[row][col] == "#":
                    swap(row, col, free_space)
                    free_space -= 1

                #if its an obstacle we need to find where the next available free space would be 
                if boxGrid[row][col] == "*":
                    free_space = col - 1
        print(boxGrid)
        #rotate the matrix to its desired form 
        #technically creating an n by m matrix and filling its row with the modified original matrix's col in reverse order
        
        #creating n by m matrix 
        res = []
        for col in range(num_cols):
            row_arr = []
            for row in range(num_rows):
                row_arr.append(0)
            
            res.append(row_arr)
        
        #filling res's row with modified original matrix's col in reverse order
        for row in range(len(res)):
            for col in range(len(res[0])):
                res[row][col] = boxGrid[col][row] 

        #need to reverse res's arrays 
        for row in range(len(res)):
            res[row].reverse()
        return res


        

