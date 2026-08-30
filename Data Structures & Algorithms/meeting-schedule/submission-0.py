"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
            Intuition:
            We are basically asked if we can find overlaps between every single adjacent 
            pair of meetings or not.

            If we find overlaps between any single pair of adjacent meetings then we
            have conflicts

            If we don't find any overlaps between any single pair of adjacent meetings
            we don't have conflicts 

            Approach
            As this is a classic interval problem asking us to identify overlaps we make
            our lives easier by analyze each interval pair from left to right aka 
            sorting each interval by start time

            Given the example:
            intervals = [(0,30),(5,10),(15,20)] (sorted by start time)

            We have an overlap between two intervals x and y where x comes first if the end 
            time of x is greater than the start time of y 

            In the example our first meeting overlaps with the meeting after it so there is 
            a conflict and thus we cannot add all meetings to our schedule

            Given the example:
            intervals = [(5,8),(9,15)] (sorted by start time)

            We don't have any overlaps in intervals here so we can add all meetings to our 
            schedule without any overlapping conflicts 
        '''

        can_attend = True

        intervals.sort(key=lambda item: item.start)

        #since we are checking for the next interval iterate all the way from 0 to one before the last interval
        #if there are no intervals this loop won't run 
        #if there is one interval this loop won't run either 
        for i in range(len(intervals) - 1):
            current_interval = intervals[i]
            next_interval = intervals[i + 1]

            if current_interval.end > next_interval.start:
                can_attend = False

        return can_attend