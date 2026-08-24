class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
          x--x
            x-x
        x--x
        --------
        01234567

        Notice that it would be intuitive to first insert the newInterval in the intervals

        Then resort the intervals array in ascending start time order 

        After insertion we can take another pass to merge overlapping intervals in the
        order given by intervals' start time
        
        when we merge we typically look at intervals from ascending start time order to
        perform
        our merge logic - aka if the start time of the incoming interval is less than the
        start time of our current interval then we merge - O(n) time 
        '''

        intervals.append(newInterval)
        intervals.sort(key=lambda item: item[0])
    
        #res will contain final merged intervals
        res = [intervals[0]]
        #merge intervals 
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])

        return res

