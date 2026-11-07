class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            constraints:
            1. pre req pairs are unique 
            2. a != b
            3. can a course have multiple pre reqs

            [0,1]
            1<-0 in order to take course 0 we must have been able to take
            course 1. we are since course 1 has no pre reqs aka no outgoing
            edges

            [[0,1],[1,0]]

            1<-0
            0<->1 since there is a cycle in this graph we are unable to take
            both courses 

            Approach 
            map every course to its pre reqs
            perform a DFS graph traversal on every course 
            if we can traverse the graph formed at the node at the given
            course then this sequence is valid 
            else its not and we encounter a duplicated in our visited set 

            Our graph is going to be represented as an adjacency list 
            
            runs:
            valid 
            [[0,1], [1, 2], [2, 3]]

            0 -> 1 -> 2 -> 3

            0 -> 1 -> 2 <-> 3
        '''
        #all our courses are from 0 to numCourses - 1
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        #set a course's list of pre reqs if applicable 
        #courses -> list of pre reqs
        #course : []

        for course, pre in prerequisites:
            graph[course].append(pre)

        #node is the current node in iteration and visited is the list of all visited nodes in our current sequence 
        def dfs(node, visited):
            #if a course has no pre reqs it can be taken
            if graph[node] == []:
                return True 

            #schedule is not valid since each class depends on each other - loop
            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if not dfs(nei, visited):
                    return False 

            #we only want to pop from visited after exploring all neighbor nodes with node       
            visited.remove(node)

            #if class, aka node forms a valid schedule then we should automatically return True for it in the future 
            graph[node] = []

            #we are able to visit all of node's neighbors without issues so we propagate True 
            return True

        #run dfs on every course in this graph to see if its a valid schedule - we will not run into loops in graph traversal 
        visited = set()
        for i in range(numCourses):
            if not dfs(i, visited): 
                return False
        
        return True


