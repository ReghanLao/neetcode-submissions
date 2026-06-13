class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:   
        self.stack.append(val)
        
        #keeping track of minimum associated with a node on original
        #stack
        if self.min_stack:
            if self.min_stack[-1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        #pops from og and min to account for the fact
        #that the min for a node might be that node itself 
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #this obtains the current minimum
        return self.min_stack[-1]