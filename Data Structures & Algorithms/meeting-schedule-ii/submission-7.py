"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
    The key idea when deciding whether or not to allocate more rooms is to
    determine whether or not a meeting conflicts with another 

    For example
    (0,40) and (5,10) conflict so they have to be in seperate rooms (first
    meeting's end time is after the second meeting's start time)
    (5,10) and (15,20) do not conflict so they can be put into the same rooms 

    On the contrary when thinking about putting meetings in the same room 
    let's think where should we put the incoming meeting?

    We want to pair the incoming meeting with a meeting in a room st that the meeting in that room ends as early as possible. This way we reduce the chances of meeting conflicts when meetings are placed in the same room

    It's better to put (15,20) in the same room as (5,10) as the meeting (5,10) ends earlier allowing (15,20) to not conflict or conflict less as opposed to putting (15,20) with (0,40) which ends later

    To simulate the idea of rooms we will use nodes in a heap. Since we need access to the room with the most recent ending time we will use a min heap since a min heap's root will contain the earliest ending time in our case 

    To form new meeting rooms we create new entries in the heap to put meetings together in the same room we pop the old meeting in the room and push the new meeitng into the same room indicating the room's new end time 

    In the end we will have allocated x rooms where x is the number of minimum rooms to schedule all meetings w/o any conflicts 
'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #heap is a min heap which stores end times of all meetings and whose root stores the room with the minimum end time
        heap = []

         #naturally we need to analyze meetings in the order in which they start aka from left to right on a number line - this intuitively allows us to scan whether the sequence of meetings will produce conflicts or not 

        #before we initialize the heap with the first meeting we need to know what the first meeting from left to right on a number line is 
        intervals.sort(key=lambda interval: interval.start)

        #there is at least 1 room required for a list of meetings greater than or eq to 1
        if len(intervals) < 1:
            return 0
        else:
            heap.append(intervals[0].end)

        #through determining conflicts between pairs of meetings we determine to allocate new room / new node in heap 
        for i in range(1, len(intervals)):
            #does the current incoming meeting conflict with the meeting with the minimum end time aka the meeting that we can best pair it with? if so then we need a new room else we don't

            #meeting w min end time ends on or before incoming interval starts thus no conflict we just need to update this meeting room's end time
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            #there is a conflict with the current incoming meeting and the meeting we would have been able to otherwise pair it with in the same room we need to create a new room for this meeting on the heap
            else:
                heapq.heappush(heap, intervals[i].end)
       
        #at the end the number of rooms is dictated by the number of nodes on heap
        return len(heap)


