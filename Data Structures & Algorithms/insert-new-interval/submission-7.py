class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
            Input array consists of non overlapping intervals and sorted in 
            ascending start time 

            Inserting newInterval can cause overlapping conflicts to arise 

            We want to resolve overlapping conflicts when inserting newInterval

            The simplest way to do this is to first insert the original non conflicting
            intervals that come before the new interval into an output array as we can use 
            extra space 
            
            and then merge all intervals that are conflicting with the
            newInterval and after that insert this new merged interval into the output arr
            
            and then insert all original intervals that are non conflicting and 
            come after the newInterval in the output array as well 

            Pretty efficient as we at most step over n entries in the original input

            Intervals are non-overlapping if they have no common point. For example, [1,2]  
            and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

            Examples:
            Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [3,7]

            [1,2] comes before so we insert as normal in output
            [3,7] is conflict with our [3,5] so we merge those two
            [9,10] comes after so we insert as normal to the ouput 

            intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

            [1,2] comes before the new interval so we insert as normal in output

            we try to insert [4,8] but it overlaps with [3,5] as its end value is greater
            than [3,5] 's start -> merge and this becomes [3,8]
            we try to insert [3,8] but it overlaps with [6,7] as its end value is greater than [6,7] 's start -> merge and this becomes [3,8]
            we try to insert [3,8] once more but it overlaps with [8,10] our newInterval becomes [3,10] no more overaps so we can insert 

            [12,16] comes after the new interval so we insert as normal in output 
        '''

        output = []

        #pointer i will track where we are in the input array at all times
        i = 0 

        #insert all original intervals that come before newInterval
        #the current interval's end time is less than the newInterval's start aka it comes before it on a number line 
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                output.append(intervals[i])
            else:
                break
            i += 1


        #now newInterval will be inserted in the output but first it needs to be merged 
        #overlapping intervals
        while i < len(intervals):
            #if the current interval is overlapping new interval merge it 
            if newInterval[1] >= intervals[i][0]:
                newInterval = [
                    min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])
                    ]
            #else break as now we have reached intervals that come after new interval 
            else:
                break
            
            i += 1


        #append newInterval before proceeding 
        output.append(newInterval)

        #insert intervals that come after newInterval
        while i < len(intervals):
            output.append(intervals[i])
            i += 1

        return output 

