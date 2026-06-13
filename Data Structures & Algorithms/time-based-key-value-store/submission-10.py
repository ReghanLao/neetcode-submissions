class TimeMap:

    def __init__(self):
        self.time_kvp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_kvp:
            self.time_kvp[key] = []
        self.time_kvp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_kvp:
            arr = self.time_kvp[key]
        else:
            arr = []

        res = ""

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
                


