from collections import defaultdict 

class TimeMap:

    def __init__(self):
        self.time_kvp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_kvp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #if set was previously called then time_kvp populated
        if key in self.time_kvp and self.time_kvp[key]:
            most_recent_ts = -1
            value = ""
            for val, ts in self.time_kvp[key]:
                if ts <= timestamp and ts > most_recent_ts:
                    value = val
                    most_recent_ts = ts
            return value
        else:
            return ""
