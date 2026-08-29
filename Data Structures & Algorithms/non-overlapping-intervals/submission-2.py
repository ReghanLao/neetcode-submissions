class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
            Refer to Callanote
        '''

        #sort input intervals to iterate thru them from 'left to right'
        intervals.sort(key=lambda item: item[0])

        #will store all intervals that are non overlapping after removing the minimum number of overlapping intervals
        #initialize to the first interval as the first interval is always 'clean'
        cleaned = [intervals[0]]

        #iterate through intervals and greedily remove later ending interval between two intervals if an overlap exists 
        #remember we are not merging intervals we are only adding intervals to cleaned if its clean or if there does indeed exist an overlap we just add the earlier ending interval 
        for i in range(1, len(intervals)):
            #there is an overlap so we just 'remove' the interval with the later end date 
            if cleaned[-1][1] > intervals[i][0]:
                #if the incoming interval's end date is earlier we want to keep this interval as future intervals are more inclined to survive after this end date aka less collisions would occur if we keep an earlier end date
                if intervals[i][1] < cleaned[-1][1]:
                    cleaned.pop()
                    cleaned.append(intervals[i])
                #else the incoming interval has a later end date we keep the current interval or they have the same end date we can just keep the current interval as end dates are the same 
                
            #no overlaps exist so this interval is 'clean' and we can append as usual
            else:
                cleaned.append(intervals[i])
        
        print(intervals)
        print(cleaned)
        #the number of removed intervals can be found thru the formula
        return len(intervals) - len(cleaned)


