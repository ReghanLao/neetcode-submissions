from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        curr_area = 0 
        visited = set()

        row = len(grid)
        col = len(grid[0])

        def bfs(r, c):
            queue = deque([])
            queue.append((r,c))
            visited.add((r,c))
            
            directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

            curr_area = 0 

            while queue:
                curr_r, curr_c = queue.popleft()
                curr_area += 1
                #exploring the current coordinate's potential neighbors
                for direction in directions:
                    dir_r = direction[0]
                    dir_c = direction[1]

                    #ensure the next coordinate we are about to visit and expand into is in bounds and hasn't been visited yet and 
                    #ensure that it is also a 1
                    if (0 <= curr_r + dir_r < row and 0 <= curr_c + dir_c < col and
                        grid[curr_r + dir_r][curr_c + dir_c] == 1 and 
                        (curr_r + dir_r, curr_c + dir_c) not in visited):
                            queue.append((curr_r + dir_r, curr_c + dir_c))
                            visited.add((curr_r + dir_r, curr_c + dir_c))
            return curr_area
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = bfs(r,c)
                    max_area = max(curr_area, max_area)
        
        return max_area


