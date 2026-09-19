"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        We want to iterate through every interval in number line order 
        (input sorted by starting time) - allows us to determine which intervals
        or meetings come first 

        At the barebones level, we can insert interval x in the same meeting room
        as an interval y if interval y is already in the meeting room and interval
        y's end time is <= interval x's start time 

        We will utilize a heap to store intervals'/meetings' end times to tell us
        whether or not we can fit our current interval in the same room as the
        interval with the min end time

        Why fit with min end time?

        We want to place intervals in the same rooms as intervals with the min
        end time because this will allow future intervals that we iterate through
        later which have start time x survive more easily allowing us to 
        cram and fit more meetings into one room 
        '''

        if len(intervals) == 0:
            return 0 

        #sorts by intervals.start
        intervals.sort(key=lambda item: item.start)        

        #will store intervals.end
        heap = [intervals[0].end]
        
        #for every interval after the first compare the incoming interval's start time with the min end time on heap

        #if we can fit in incoming interval after min end time - insert aka pop min end time and update it with incoming interval end time aka heappush the new interval's end time

        #if we can't fit in incoming interval after min end time - insert regardless aka heappush incoming interval end time signifying a new meeting room with the interval's end time now exists 
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            
            #after fitting incoming interval update end time for that room 
            #or if can't fit create new meeting room for this meeting 
            heapq.heappush(heap, intervals[i].end)

        #the number of meeting rooms required is the len of the heap
        return len(heap)
