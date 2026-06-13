class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #we are going to partition the array into three regions
        #a region with zeros, a region with ones, and a region with twos 
        #lets put the zeros at the left and place the twos at the right 
        #as a result the ones will naturally fall into the middle of the array 
        #if we perform a right swap lets not advance our i pointer as we can introduce 0s in the middle of our array thru swapping
        #once our i ptr surpasses our right ptr we are done

        #When swapping a 0 to the left, the element swapped in comes from the 0s or 1s region (already correct) so we can safely advance i, but when swapping a 2 to the right, the element comes from the unknown region and could be a 0, 1, or 2, which might introduce a 0 into the middle, so i must be rechecked before advancing.
        l = 0 
        r = len(nums) - 1
        i = 0 

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            i += 1
