class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
            Brute Force Approach:
            Go through every single pair of bars and calculate the area that can be formed
            from bar i to bar j where the height of this range is determined by the shortest
            height in this range

            Inefficient because we are repeatedly checking bar heights that we have 
            potentially checked before 

            Optimal Approach:
            Instead of blindly repeatedly checking bar heights we have seen before

            We are able to extend a bar in the graph in both directions - backward
            or forward if the the height of the bar is less than or
            equal to the bars that surround it

            We are unable to extend a bar any further in any direction if its 
            height exceeds those that surround it - either forward or backward 

            We want to find the best area from extending every single bar in the 
            histogram  

            Approach:

            We can do this by iterating through every bar and seeing how far we can 
            extend this bar. 

            Once a bar is no longer able to be extended we should note the area that
            is formed thru this bar and remove it from consideration

            Since we have the ability to extend bars backwards we should use a stack
            to keep track of bars and the indicies that they occur on so we can have
            reference to the index that a previous bar occured on and then be able to 
            extend back to that index if possible when that previous bar is removed 
            from consideration

            item on stack -> (index, bar_height)

            We calculate every single area possible from extending all bars and 
            return that area 
        '''

        #stores (index, height) tuples 
        stack = []
        area = 0

        #iterate through every single bar height and see how far we are able 
        #to extend a particular bar height 
        for i in range(len(heights)):
            #used to note the start index of the incoming bar - it can be i 
            #or if it can be extended backward when the bars on the stack are too 
            #tall then it will be set to one of those bars' indicies 
            start_index = i
            #while we can no longer extend a particular bar we need to remove it from consideration,
            #calculate the area that is made possible by this bar height, and note the index of this 
            #now invalid bar so we can extend our current bar backward 
            while stack and stack[-1][1] > heights[i]:
                prev_index, prev_height = stack.pop()
                
                #i is the index we cannot extend up to anymore, so i - prev_index is the
                #valid width that this rectangle will get
                area = max(area, prev_height * (i - prev_index))
                start_index = prev_index


            #we can keep extending bars forward - start index determined as noted above in earlier comment
            stack.append((start_index, heights[i]))

        #at the end there will be some bars taht can be extended to the end aka 
        #there will be bars on the stack still - we should calculate the area that can be 
        #formed via this bars

        for start_index, height in stack:
            area = max(area, height * (len(heights) - start_index))
        
        return area 