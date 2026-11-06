from collections import deque 
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        '''
            constraints:
            1. empty graph -> empty graph 
            2. graph is connected so we cannot have 1 2 3 
            3. no loops in graph 

            input: 
            a singular node reference

            deep copy -> all the nodes of the new graph cannot point to the references of nodes in the old graph 

            Approach 
            1. Map every original node to every single new node we want to create 
            2. Using the old graph's relationships we connect new nodes together and form the deep copy 

        '''
        #old nodes to new nodes
        #'base case' our graph that we want to copy is empty so we map it to an empty graph 
        if node is None:
            return None
        mapping = {}

        #run a BFS on graph made by node 
        q = deque([node])
        visited = set()
        visited.add(node)

        #mapping every node in original graph to be a new node to ensure we can create a deep copy later using the original graph's rls
        while q:
            node = q.popleft()
            mapping[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        
        #link together the new nodes using the original graph's relationships 
        #iterate through all the nodes in the mapping these are all the nodes we have to form rls with each other 
        for node, _ in mapping.items():
            #for every single original neighbor rls st these neighbor nodes are mapped to new nodes we append these neighbors to our new node to set the rls 
            for nei in node.neighbors:
                neighbor = mapping[nei]
                mapping[node].neighbors.append(neighbor)

        one_ref = None 

        #obtain reference to 1
        for key, _ in mapping.items():
            if key.val == 1:
                one_ref = key
                break

        #reeturn reference to 1
        return mapping[one_ref]