from collections import deque 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            Run a BFS on every cell in the grid if it is a land cell which
            hasn't been explored yet and calculate the area that we can
            obtain starting our expansion from that land cell 

            Return the maximum area that can be obtained starting from every
            landcell
        '''     
        n = len(grid)
        m = len(grid[0])

        max_area = 0 

        #seen stores nodes (i, j)
        seen = set()

        #return the area that can be obtained from expanding at src 
        #(i, j)
        def bfs(i, j, seen):
            #q stores nodes (i,j)
            q = deque()
            q.append((i,j))
            seen.add((i,j))

            #area of island starting at (i,j)
            area = 0

            directions = [ [0, -1], [0, 1], [-1, 0], [1, 0] ]
            
            while q:
                node = q.popleft()
                node_row, node_col = node

                area += 1 
                #for every node that we visit we need to visit its potential neighbors that are potentially land nodes horizontally or vertically 
                for direction in directions:
                    new_row = node_row + direction[0]
                    new_col = node_col + direction[1]

                    if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1 and (new_row, new_col) not in seen:
                        q.append((new_row, new_col))
                        seen.add((new_row, new_col))

            return area 

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = bfs(i, j, seen)
                    max_area = max(max_area, area)

        return max_area 