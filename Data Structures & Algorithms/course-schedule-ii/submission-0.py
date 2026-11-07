class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #three clear states: nodes on path and nodes already confirmed and visited, and nodes that haven't been visited 

        #represents the nodes in our current recursion path
        path = set()
        
        #represents the nodes that we have confirmed to be possible/True and now can be added to topological outpt
        visited = set()

        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        #populate graph with a course -> pre req
        for course, pre in prerequisites:
            graph[course].append(pre)

        output = []

        #all of our graph traversals will share state for current nodes in path and nodes that have been visited in prev iterations since we don't want to revist nodes that have been visited to preserve topological order. 
        def dfs(course):
            if course in path:
                return False 
            
            if course in visited:
                return True 
            
            path.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            #we can take all neighbor / pre req courses so we can now take course
            path.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output