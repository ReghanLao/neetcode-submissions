class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #init sum_matrix with zeros 
        #account for edge case where we want to calculate sum of a smaller rectangle, 
        #but there is nothing to the left or above it so we initialize 0s above and to the left - adding 0 does nothing
        self.sum_matrix = []

        for i in range(len(matrix) + 1):
            zeros = []
            for j in range(len(matrix[0]) + 1):
                zeros.append(0)
            
            self.sum_matrix.append(zeros)
        
        #creates prefix sums for rectangles within matrix 
        #the prefix sum of every single row acts as a building block
        #for the prefix sums of rectangles 
        for i in range(len(matrix)):
            prefix = 0
            for j in range(len(matrix[0])):
                prefix += matrix[i][j]
                above = self.sum_matrix[i][j + 1]
                self.sum_matrix[i + 1][j + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1

        #A represents the sum of the whole rectangle up to the bottom right
        #B represents the sum of the rectangle above
        #C represents the sum of the rectangle to the left
        #D represents the sum of the top left
        #sum of sub rectangle = A - B - C + D
        A = self.sum_matrix[row2][col2]
        B = self.sum_matrix[row1 - 1][col2]
        C = self.sum_matrix[row2][col1 - 1]
        D = self.sum_matrix[row1 - 1][col1 - 1]

        return A - B - C + D


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)