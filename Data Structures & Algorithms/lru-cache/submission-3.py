class Node():
    def __init__(self, key, val, nxt, prev):
        self.key = key
        self.val = val 
        self.nxt = nxt 
        self.prev = prev

class LRUCache:
    #O(1) time to fetch val associated with key quickly so we use a  hashmap 
    #we need a way to keep track of the most recently used area 
    #and least recent used area efficiently -> doubly LL as access to head (LRU) and tail (MRU) are constant
    def __init__(self, capacity: int):
        #key -> node (key, val)
        #important to store key, val in node because when we remove the LRU from LL 
        #we need a key reference to remove from the hashmap as well 

        self.cache = {}
        self.size = capacity 

        #LRU is head and MRU is tail 
        #sandwiching nodes in between LRU and MRU as these are just pointer nodes
        self.lru = Node(0, 0, None, None)
        self.mru = Node(0, 0, None, None)

        self.lru.nxt = self.mru
        self.mru.prev = self.lru

    #removes node from current position in doubly LL 

    # o <-> o <-> o
    def remove(self, node):
        prev = node.prev 
        nxt = node.nxt 

        prev.nxt = nxt 
        nxt.prev = prev

        node.nxt = None 
        node.prev = None 


    #inserts before MRU and after previous node 
    def insert(self, node):
        prev = self.mru.prev

        node.nxt = self.mru
        node.prev = prev

        self.mru.prev = node
        prev.nxt = node


    def get(self, key: int) -> int:
        if key in self.cache:
            #when we get a key is considered used so its move to MRU section
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            #a key is considered used to move to MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else: 
            #a key is considered used to move to MRU
            node = Node(key, value, None, None)
            self.insert(node)
            #insert into cache 
            self.cache[key] = node
        
        if len(self.cache) > self.size:
            #remove the node LRU points in doubly LL and delete it from the cache
            node_to_remove = self.lru.nxt
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]




