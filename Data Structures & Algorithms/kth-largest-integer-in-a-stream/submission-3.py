'''
    Naive Approach: 
    Let n be the size of the initial stream of integers

    Init:
    Initialize an array containing elements in nums and a const k - O(n) where n
    is the initial size of the stream 

    Per call TC - O(n)

    Add:
    Add element to array - O(1)

    Sort array everytime an element is added - per call i it would be
    O((n+i)log(n+i))

    The kth largest in sorted order counting duplicates exists k positions from
    the end as we - accessing this index is O(1)

    Per Call i TC - O(1) + O((n+i)log(n+i)) + O(1) = O((n+i)log(n+i))
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums.copy()
        self.k = k

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        return self.stream[len(self.stream) - self.k]

