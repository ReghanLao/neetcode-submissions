class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        #we sort the current stream
        #the kth largest element in the stream is k steps back from the largest element
        #this is basically at n - k when the stream is sorted
        self.nums.append(val)
        sorted_nums = sorted(self.nums)
        n = len(sorted_nums)
        
        #the kth largest is k steps back from n 
        return sorted_nums[n - self.k]
