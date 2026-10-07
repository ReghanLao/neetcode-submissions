import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            Two heaviest stones -> concerned about the two heaviest 
            
            The best way to access a max element or in this case the two 'max
            elements' effciently is to use a max heap

            We want to store all elements in a max heap and inspect the top two
            nodes x and y at a given point 

            Perform the respective comparisions 
            1. if x == y then pop both 
            2. if x < y then pop x and update y to be y - x

            Continue while len of heap > 1 (number of stones left to break)
        '''
        heap = stones.copy()
        #we will heapify stones and convert it to a max heap 
        heapq.heapify_max(heap)
        #while there is more than one stone we need to see if we can destory them
        while len(heap) > 1:
            y = heapq.heappop_max(heap)
            x = heapq.heappop_max(heap)

            #if x and y are equal then they are both destroyed but if x and y are not equal and x < y then x is destoryed and y is y - x
            #in other words we just push y - x onto the heap
            if x != y and x < y:
                heapq.heappush_max(heap, y-x)
        
        #check for the length of the heap if there is a remaining stone return that weight else return 0 
        print(heap)
        if len(heap) > 0:
            return heap[0]
        else:
            return 0 

