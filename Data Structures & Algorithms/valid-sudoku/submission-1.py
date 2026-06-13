class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        #checking if rows are valid 
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] not in {"1","2","3","4","5","6","7","8","9"} or board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        
        #checking if columns are valid 
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[j][i] != ".":
                    if board[j][i] not in {"1","2","3","4","5","6","7","8","9"} or board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])

        #checking if each of 3x3 boxes are valid 
        #outer 2 for loops define the boundaries of boxes 
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                #inner 2 for loops go thru each element in these boxes to check if valid
                for i in range(3):
                    for j in range(3):
                        if board[box_row + i][box_col + j] != ".":
                            if board[box_row + i][box_col + j] not in {"1","2","3","4","5","6","7","8","9"} or board[box_row + i][box_col + j] in seen:
                                return False
                            else:
                                seen.add(board[box_row + i][box_col + j])

        return True

