class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
            A good way to look at this problem is to plot intervals
            on a number line and merge them / consolidate them from 
            left to right 

            How do we know when to merge an interval?

            if the start of the next succeding interval's start is 
            less than the current interval's end then we change this
            current interval to include the next succeeding
            interval's end value

            How would we process a list of intervals?

            In the order of starting position first. Looking at the 
            example [[4,7],[1,4]] its clear that for the merge logic 
            to properly operate we need to sort the array of lists by 
            starting position.

            If the start positions are the same we want to have the 
            left most interval be processed first so sort by first
            start position and fall back to end position if starts
            are the same - [[1,2], [1,3]] is a good example
        '''

        #we want to merge intervals on a number line from left to right - if same start fall back to second position to process left most intervals first 
        intervals = sorted(intervals, key=lambda item: (item[0], item[1]))

        #initialize res with the first interval because we are guaranteed to have one interval 
        res = [intervals[0]]

        #iterate through remaining intervals from left to right 
        for i in range(1, len(intervals)):
            #if current (res list) interval's ending value is greater than the next (interval list) interval's start value then we can merge these two into one interval
            if res[-1][1] >= intervals[i][0]:
                #by assiging we are merging
                res[-1] = [res[-1][0], max(intervals[i][1], res[-1][1])]
            else:
                #by appending we are not merging two intervals but propagating original 
                res.append(intervals[i])

        return res

