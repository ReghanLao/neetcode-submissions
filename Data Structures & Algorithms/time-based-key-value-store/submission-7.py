import math

class TimeMap:

    def __init__(self):
        self.time_kvp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_kvp:
            self.time_kvp[key] = []
        self.time_kvp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        most_recent_ts = -math.inf
        most_recent_val = ""

        if key in self.time_kvp and self.time_kvp[key]:
            for val, ts in self.time_kvp[key]:
                if ts <= timestamp:
                    most_recent_ts = ts
                    most_recent_val = val

        return most_recent_val


