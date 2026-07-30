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
    '''
    def get(self, key: str, timestamp: int) -> str:
        res = ""

        for ts, value in self.store[key]:
            #we need to make sure that the timestamp for this particular value is <= the query timestamp
            if ts <= timestamp:
                res = value
            else:
                break

        return res
