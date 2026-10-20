from collections import defaultdict
class TimeMap:

    def __init__(self):
        #key -> list of (val, time)
        #defaultdict of lists
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #return a value where the prev time stamp is as close to timestamp as possible if not equal to it 

        #naive approach for a given key iterate over all entries st its timestamp <= query timestamp

        #if we have a set of timestamps for a key like 1 2 3 4 5 and our query ts is 5 why would we want to check earlier ts like 1 2 3 lets use a BS to accurately narrow our search space. this will improve our TC from O(m) where m is the number of entries for a particular key to log(m)

        #this works because the timestamps of set are strictly increasing and python dicts perserve insertion order so the entries are technically sorted by TS 
        res = ""
        l = 0 
        r = len(self.mapping[key]) - 1

        while l <= r:
            m = (l + r) // 2
            ts = self.mapping[key][m][1]
            val = self.mapping[key][m][0]
            #if we find a candidate timestamp that is less its a potential valid answer but lets try to find smth closer to query or if we find a cnaidate timestamp that is equal to time stamp then its a valid ans
            if ts <= timestamp:
                res = val
                l = m + 1
            #ts at mid > query timestamp - need to eliminate these greater options and look for smaller ts
            else:
                r = m - 1
            
        
        return res
