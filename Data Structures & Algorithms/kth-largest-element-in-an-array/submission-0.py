import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            When we think of the kth largest/smallest -> heap since heap 
            managaes this for us thru its structure automatically 

            If we maintain a min heap of size k as we iterate through the 
            array we will naturally maintain the kth largest elements of 
            the array til a given index i if we do this to the end
            we will main the kth largest elements of the array til the end
            aka the kth largest elements in the entire array were our root
            is the kth largest 

            for every element n 
                perform log k heap operation (either pushing - init or
                popping - maintain heap size)
        '''

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            #since we only ever add one element at a time a one time check for overflow is enough
            #remove the smallest element at index x so that once we get to the end at index i we will have the root point to the kth largest element we received from iterating through the entire array
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]