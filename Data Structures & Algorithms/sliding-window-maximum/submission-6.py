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
            element so we repeatly pop these elements

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

        #store indicies on our queue to check for the possibility of our maximum element being out of bounds
        q = deque()
        left = 0 


        res = []

        for right in range(len(nums)):
            #since our deque is in monotonically decreasing order and we only ever want to consider the maximal element for our current given window if we are about to add an element to our window and its greater than all other elements in the deque/window we should never have to consider these elements on our deque as potential candidates to be maximiums in future windows because not only are they smaller but they come before the most recent greater element 
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)
            
            #check if maximal element index is out of bounds if so remove from consideration
            if q[0] < left:
                q.popleft()

            #return the most current/accurate maximal element for the current window 
            if right - left + 1 == k:
                res.append(nums[q[0]])
                left += 1
            
            

        return res

        