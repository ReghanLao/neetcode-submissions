class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val

        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map keys to nodes 

        #left -> LRU and right -> MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        #these left and right nodes need to be connected to each other 
        #because new nodes go in between them
        self.left.next = self.right
        self.right.prev = self.left
    
    #removing from left -> LRU
    def remove(self, Node):
        prev, nxt = Node.prev, Node.next
        prev.next = nxt
        nxt.prev = prev

    #inserting at right -> MRU
    def insert(self, Node):
        #prev node is the node before right 
        #next node for this node is just right
        prev = self.right.prev
        nxt = self.right 

        prev.next = Node 
        nxt.prev = Node

        Node.prev = prev 
        Node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            #update to most recent after access
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove LRU from LL and del LRU element from cache
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
