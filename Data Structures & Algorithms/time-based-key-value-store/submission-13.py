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
        res = ""

        for val, ts in self.mapping[key]:
            if ts <= timestamp:
                res = val
            else:
                break 

        return res
