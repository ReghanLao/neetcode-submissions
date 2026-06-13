from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #run a BFS starting from every single land cell -> we can simultaneously explore
        #all paths and determine (return) when we find the best path to the treasure

        #for every level that we visit / every neighbor we expand out to we 
        #increment our distance 

        #if we find a treasure cell we can update the land cell we started BFS from
        #with the distance traveled to this land cell 

        def bfs(r, c):
            queue = deque([(r,c)])
            #keep track of visited cells so we don't unnecessarily revist them
            visited = set()
            visited.add((r,c))

            directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]

            distance = 0 
            while queue:
                #pop all nodes on our current level and append all neighbors
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    #check if the curr position is a 0 if so then return distance
                    if grid[row][col] == 0:
                        return distance

                    #append all neighbors 
                    for direction in directions:
                        new_row = row + direction[0]
                        new_col = col + direction[1]
                        #ensure new direction is in bounds then we can visit 
                        #ensure we can visit it != -1
                        #ensure we haven't visited it 
                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != - 1 and (new_row, new_col) not in visited:
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
                            
                distance += 1  

            #we never reach a treasure so we return 
            return 2147483647


        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r,c)

