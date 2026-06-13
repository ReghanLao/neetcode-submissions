class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                # Row check
                row_val = board[i][j]
                if row_val != ".":
                    if row_val not in "123456789" or row_val in row_set:
                        return False
                    row_set.add(row_val)

                # Column check
                col_val = board[j][i]
                if col_val != ".":
                    if col_val not in "123456789" or col_val in col_set:
                        return False
                    col_set.add(col_val)

        # 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != ".":
                            if val not in "123456789" or val in box_set:
                                return False
                            box_set.add(val)
        return True
