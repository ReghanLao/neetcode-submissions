class Solution:
    def reverse(self, left, right, arr):
        while left < right: 
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left += 1
            right -= 1
        
    
    def rotate(self, nums: List[int], k: int) -> None:
        #reverse array -> places elements in relative position compared to rotated counterpart
        #reverse first k elements -> fixes order of first k elements
        #reverse remaining elements -> fixes order of remaining n - k elements 

        #reversals break unless k is reduced to a valid index range
        #shifting by k steps is = shifting by k % n steps 

        k = k % len(nums)
        self.reverse(0, len(nums) - 1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums) - 1, nums)





        