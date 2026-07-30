'''
Note:
Insertion order of a dictionary is preserved 

Regardless, all timestamps of set are set in an increasing order
So for a particular key the list of (timestamp, value) tuples 
are sorted by timestamp in increasing order by default 
'''
from collections import defaultdict

class TimeMap:

    '''
    key -> list of (timestamp, value) tuples 
    '''
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    '''
    return a value associated with the given key which has a time
    which has a timestamp value less than or equal to the query 
    timestamp 

    we want to return the value associated with the largest 
    prev time stamp value if there are multiple previous existing 
    time stamps aka the most recent time stamp

    can't assume that every single timestamp in our store will be less than or equal to our query time stamp - we might have greater time stamps 

    we don't need to go through every single timestamp value entry in our store because some of them are inherently just so far away from our query timestamp that checking over them would be useless

    lets intelligently narrow our search space st we get closer and closer to the query time stamp without iterating over timestamps that are either too small or too large 

    we can do this using a BS 
    '''
    def get(self, key: str, timestamp: int) -> str:
        res = ""

        left = 0
        right = len(self.store[key]) - 1

        while left <= right:
            print(self.store[key])
            #our mid point is basically the candidate entry that we are evaluating 
            mid = (left + right) // 2

            #lets evaluate our candidate's timestamp value 
            ts = self.store[key][mid][0]

            #if the time stamp we are looking at is <= our query timestamp this could be an answer but theres also a chance a more larger stamp value exists for this key so lets look right
            if ts <= timestamp:
                print(ts)
                print(self.store[key][mid][1])
                res = self.store[key][mid][1]
                left = mid + 1
                print(left)
                print(right)
            else:
                #if the timestamp we are looking at is > that our query all the entries after this and including this is completely irrelevant lets look left 
                right = mid - 1
            
        return res
