class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''

        constraints:
        array cannot be empty 
        k > 1
        x is any number between -10,000 and 10,000

        approach:
        since we only want to consider a candidate set of k elements 
        we can consider the set of all elements in this array as part of our 
        candidate set of k elements 

        n - k 

        1. iterate through the array 
        2. calculate every window of size k 
            how far its elements are away from x
            find the total distance of the window from x
            keep the window with the smallest distance 

        '''
        min_dist = float('inf')
        res = []

        for i in range(len(arr) - k + 1):
            window = arr[i:i+k]

            dist = sum(abs(num - x) for num in window)

            if dist < min_dist:
                min_dist = dist 
                res = window 

        return res