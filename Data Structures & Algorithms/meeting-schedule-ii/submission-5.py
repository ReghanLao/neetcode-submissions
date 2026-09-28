"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''

(0,2), (1,3), (2, 5)

BAD:
room1: (0,2)
room2: (1,3)
Room3: (2,5)

GOOD:
room1: (0,2), (2,5)
room2: (1,3)

The whole idea is to use a heap to store end times so that we are able to fit 
incoming meetings with minimum end times this way we reduce conflicts and minimize
the number of meeting rooms that we have to allocate 

'''
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda item: item.start)
        
        heap = []

        #stores meeting end times if meetings even exist
        if len(intervals) >= 1:
            heapq.heappush(heap, intervals[0].end)
        else:
            return 0 

        #go through intervals and fit incoming interval with meeting with the earliest end time so we can squeeze more meetings together else create a new room for conflict 
        for i in range(1, len(intervals)):
            #can fit the incoming meeting with min end time meeting in same room
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            
            #insert the meeting into a new room or if can be fit with min end time meeting (after its popped) put it in the 'same room'
            heapq.heappush(heap, intervals[i].end)
        
        return len(heap)
        