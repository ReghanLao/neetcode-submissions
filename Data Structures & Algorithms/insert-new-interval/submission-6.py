class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            Refer to Collanote Notes
        '''

        res = []

        i = 0

        #prepend all intervals less than newInterval first
        while i <= len(intervals) - 1 and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        #resolve the insertion of newInterval by merging it with overlapping intervals - if required or if overlaps even occur 
        while i <= len(intervals) - 1 and newInterval[1] >= intervals[i][0]:
            #we do min between the new interval's start and incoming interval's start because we are unsure which would be smaller eg: newInterval = [1,8] and intervals[i] = [2,3]
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        
        #append resolved (if applicable) newInterval 
        res.append(newInterval)

        #append all remaining intervals greater than newInterval
        while i <= len(intervals) - 1 and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1

        return res 
