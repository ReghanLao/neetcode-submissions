class TimeMap:

    def __init__(self):
        self.time_kvp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_kvp:
            self.time_kvp[key] = []
        self.time_kvp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""   
        if key in self.time_kvp:
            arr = self.time_kvp[key]
        else:
            arr = []

        #perform binary search on specified value, timestamp list 
        #as time stamps are strictly increasing
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            #valid candidate but lets try to find a timestamp
            #closer to the query time stamp in the right
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                left = mid + 1
            else:
            #calculated timestamp is too big shrink search to the left
                right = mid - 1
        
        return res
            

