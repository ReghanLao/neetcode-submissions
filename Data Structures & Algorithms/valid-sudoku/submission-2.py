class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_nums = {1,2,3,4,5,6,7,8,9}
        n = len(board)

        #iterate through every row and check conditions
        for row in range(n):
            seen = set()
            for col in range(n):
                if board[row][col] != ".":
                    if int(board[row][col]) not in valid_nums or board[row][col] in seen:
                        return False 
                    else:
                        seen.add(board[row][col])
        
        #iterate through every column and check conditions 
        for col in range(n):
            seen = set()
            for row in range(n):
                if board[row][col] != ".":
                    if int(board[row][col]) not in valid_nums or board[row][col] in seen:
                        return False 
                    else:
                        seen.add(board[row][col])
        
        #iterate through every 3x3 board and check conditions 
        
        #outer skeleton - selecting each 3x3 board
        for board_row in range(0, 9, 3):
            for board_col in range(0, 9, 3):
                seen = set()
                #traverse these boards
                for i in range(board_row, board_row + 3):
                    for j in range(board_col, board_col + 3):
                        if board[i][j] != ".":
                            if int(board[i][j]) not in valid_nums or board[i][j] in seen:
                                return False 
                            else:
                                seen.add(board[i][j])

        return True 