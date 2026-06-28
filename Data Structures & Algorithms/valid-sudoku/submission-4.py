class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            An en empty board, row, or column is 
            fundamentally valid 

            We just cannot have any duplicate values of 
            1-9 in a given row, column, or 3x3 sub grid 
        """

        #validate rows 
        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] != ".": 
                    if int(board[r][c]) not in seen:
                        seen.add(int(board[r][c]))
                    else:
                        return False 
        #validate columns 
        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] != ".":
                    if int(board[r][c]) not in seen:
                        seen.add(int(board[r][c]))
                    else:
                        return False 
        #validate 3x3 subgrids

        #outer nested loop will go through every subgrid

        #inner nested loop to go through every cell in subgrid
        for r in range(0, len(board), 3):
            for c in range(0, len(board[0]), 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] != ".":
                            if int(board[r + i][c + j]) not in seen:
                                seen.add(int(board[r + i][c + j]))
                            else:
                                return False 
        
        return True 

        