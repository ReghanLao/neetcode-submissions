from collections import deque
class Solution:
    '''
    
        Brute Force Approach:
            Sliding a window of size k over the input and considering all windows 
            of size k and determine what the maximum element is from a given window

            TC:
            For every single window we are scanning through all k elements in the
            window potentially so our worst case TC would be 

            O(num of windows * k) = O(n - k + 1 * k)

             Number of windows:
            The last valid starting index of a window is n-k.
            Since arrays are 0-indexed, the possible starting indices are:
            0, 1, 2, ..., n-k
            Therefore, the number of windows is:
            n-k+1 

        More TC Friendly Approach:
        As we shift windows we know certain elements would never be our maximum right
        For example consider this example:

        [1  2  1] 0  4  2  6        
        1 [2  1  0] 4  2  6        

        we know that for the second sliding of the window 1 would never be our
        maximum for our window because we already see a 2 

        do we need to really consider all elements when sliding this window?

        We can use a DEQUE
            As we add elements to our window we add them to our deque. If the element
            we are about to add is greater than the element on top of our deque
            how could this element in our deque aka our window ever be the maximum
            element so we repeatly pop these elements - this new element dominates
            because not only is it greater but it outlives these prior elements
            making it a better candidate to tbe the max for other windows in the
            future

            Only the elements that still have a possibility of becoming the maximum
            are STORED IN OUR DEQUE

            Why a DEQUE? 
            We are able to remove the maximum element from the front of
            our deque if its out of bounds in as our window shifts in O(1) time and
            we are able to add or remove elements at the 
            back of our deque as we add new elements to our current window in O(1)
            time

            This is a MONOTONICALLY DECREASING DEQUE

            Why is it monotonically decreasing - since we add elements to our window
            to our deque, once we encounter a larger element we want to add into our 
            window so we pop all smaller elements on our deque - note by this nature
            all elements on our deque are monotonically decreasing thus our MAX     
            Element for our window is the FIRST element 
    '''

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #when we slide the window over our maximum element may be out of bounds we need to remove it from consideration so we store indicies 
        q = deque([])

        left = 0 
        res = []

        # 1 1 1 1 4 5, k = 5
        #deque = [4, ]
        for right in range(len(nums)):
            #if our incoming element is greater than our previous maximum elements on the deque why would we ever consider those again plus this new incoming value will survive longer into the furture serving its usecase in identifying potentially the max for future windows 
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            
            q.append(right)

            window_len = right - left + 1

            if window_len == k:
                res.append(nums[q[0]])
                left += 1

            #check if our maximum on deque is still our maximum for curr window 
            #[1,2,1,0,4,2,6], k = 3
            #q = [1, 0], res = [2,2], left = 2
            if q[0] < left:
                q.popleft()

        return res
        

        #takeaway intuition: "When the window moves, most elements are the same. Can I maintain useful information instead of rebuilding it?"

        