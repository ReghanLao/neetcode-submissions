from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            Input is a grid, not an adj matrix as dimensions are
            not necessarily n * n but can still use graph BFS to
            traverse grid
            
            The idea is that we can start at a source land node 
            aka a 1 which hasn't been explored yet and expand 
            out in all directions horizonatally and vertically
            using a BFS

            Once we can longer expand outward anymore we have
            finished traversing one island and we can continue
            to search for more islands
        '''
        n = len(grid)
        m = len(grid[0])
        #set being modified inside function is also reflected outside 
        def bfs(i, j, seen):
            source = (i,j)
            seen.add(source)
            q = deque()
            q.append(source)

            #defines directions we can move in allowing us to enqueue the respective nodes onto the q for BFS traversal
            #going up is adding 1 to row value, going down is subtracting 1 from row value, going left is subtracting 1 from col value, and going right is adding  1 to row val
            directions = [[1,0], [-1,0], [0, -1], [0, 1]]

            while q:
                node = q.popleft()
                node_row = node[0]
                node_col = node[1]
                #explore all possible directions
                for direction in directions:
                    row_inc = direction[0]
                    col_inc = direction[1]

                    new_row = node_row + row_inc
                    new_col = node_col + col_inc
                    new_node = (new_row, new_col)

                    #if this new position is EVEN VALID and a land node and hasn't been visited then we can visit and add it to our current island
                    if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == "1" and new_node not in seen:
                        seen.add(new_node)
                        q.append(new_node)

        #store land nodes positions which have been visited 
        #stores (i,j)
        seen = set()
        islands = 0 

        #go through every possible source node which hasn't been
        #visited yet and perform a BFS
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in seen:
                    bfs(i, j, seen)
                    #after bfs traversal is done on src then increment num of islands by 1 - we have one more island 
                    islands += 1
        print(seen)
        return islands 