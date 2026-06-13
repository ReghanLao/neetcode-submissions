class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = []

    def get(self, key: int) -> int:
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                #has been accessed so move toward recently accessed end 
                element = self.cache.pop(i)
                self.cache.append(element)
                return element[1]
        return -1

    def put(self, key: int, value: int) -> None:
        #checking if key already exists 
        #update first then move to most recently accessed end
        for i, (k,v) in enumerate(self.cache):
            if k == key:
                self.cache[i] = (key, value)
                element = self.cache.pop(i)
                self.cache.append(element)

                return #avoid duplicate append
        
        #checking if we are are capacity 
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        
        #now we are able to add new element 
        self.cache.append((key,value))

