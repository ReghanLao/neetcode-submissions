#doubly LL node
class Node():
    def __init__(self, val, key=None, nxt=None, prev=None):
        #if we store the key as well we have access to what key to delete from the cache when we removed the LRU node from the doubly LL
        self.val = val
        self.key = key
        self.nxt = nxt
        self.prev = prev 
class LRUCache:
    #MRU <-> 1 <-> 2 <-> LRU
    def __init__(self, capacity: int):
        self.MRU = Node(0)
        self.LRU = Node(0)

        #connect MRU and LRU to chain nodes between
        self.MRU.nxt = self.LRU
        self.LRU.prev = self.MRU

        self.capacity = capacity

        #our cache maps keys to nodes 
        self.cache = {}
    
    #inserts after MRU and shifts the remainder of the doubly LL accordingly
    def insert(self, node):
        remainder = self.MRU.nxt
        self.MRU.nxt = node
        node.prev = self.MRU
        node.nxt = remainder
        remainder.prev = node
    
    #delete a given node from its position 
    def delete(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            #if the node exists we need to delete it first then reinsert it
            self.delete(self.cache[key])

            #once node has been deleted from orginal position put it after MRU
            self.insert(self.cache[key])
            #self.cache[key] returns a node
            return self.cache[key].val
        
        #key not in cache
        return -1

    def put(self, key: int, value: int) -> None:
        #if key exists node already exists in LL so we need to delete it first and move it to MRU and update its value
        if key in self.cache:
            #delete the old node from the LL then create a new node and map it to the key and then insert it into LL
            self.delete(self.cache[key])
            
            self.cache[key] = Node(value, key)

            self.insert(self.cache[key])
        else:
            #insert this node for the first time
            self.cache[key] = Node(value, key)

            #move the inserted node to MRU
            self.insert(self.cache[key])
            
            #if applicable: if the insertion caused an overflow in the cache we need to delete the node that LRU is pointing to 
            if len(self.cache) > self.capacity:
                #node to delete is pointed to by LRU 
                target = self.LRU.prev

                self.delete(target)
                #need to delete key from the hashmap as well
                del self.cache[target.key]
            
        

