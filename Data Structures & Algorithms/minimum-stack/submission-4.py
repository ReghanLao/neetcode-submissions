class MinStack:
    #every operation should run in constant time 

    def __init__(self):
        self.stack = []
        self.min_stack = []

    #every time we push a value onto our stack
    #we need to update the minimum value associated with that value
    #aka inserting in our min stack 
    def push(self, val: int) -> None:
        self.stack.append(val)

        #check if added element will be the new min for this point in time
        if self.min_stack:
            curr_min = self.min_stack[-1]
        else:
            curr_min = val
        
        new_min = min(curr_min, val)
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()    
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    '''
        how can we retrieve the minimum element in O(1) time? 
            1. we can initialize another stack (min stack) along with our 
            original stack 
            2. We can have every 'node' in our original stack be parallel
            with another 'node' in our min stack 
            3. At any given point in time, the node in the min stack will
            tell us whats the min value corresponding to a given point in 
            the original stack is 
             
            Basically the min stack tells us what the minimum value at a given
            node in the original stack is by mirroring the original stack and keeping 
            track of the minimum at any given point in time
    '''
    def getMin(self) -> int:

        return self.min_stack[-1]