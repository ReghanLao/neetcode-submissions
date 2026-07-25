class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            A solution in log n time indicates tackling this problem through a 
            Binary Search 

            An array can be rotated x times where x can either be 

            1 to n - 1 times -> rotated sorted array 
            or any multiple of n times -> original sorted array

            Notice that the minimum element appears at the peak area of the 
            rotated sorted array

            Notice that the minimum element appears at the first element of the
            original sorted array 

            We can run a BS on the input array to determine where this peak 
            occurs -> our computed middle will tell us where we are 

            if the computed middle is greater than our last element (ROTATED SORTED ARRAY) then our peak is 
            somewhere to the right visually 
            
            if our computed middle is less than our
            last element (ROTATED SORTED ARRAY) we could already be in the peak area where this minimum occuurs
            but theres a chance that a smaller element occurs to the left of it so 
            we don't want to scrap out that possibility so we look to the left while 
            keeping this computed middle element in mind 

            if our computed middle is both less than the last element and greater than the first
            element our input array is rotated a multiple of n times aka this array is already 
            sorted and in original order so we can just return the first element
        '''

        left = 0 
        right = len(nums) - 1 

        #since we aren't scraping the possibility that our computed middle could 
        #be a solution in the case where the computed middle is less than our 
        #right most value, our right ptr will still keep computed middle in mind for our range aka 
        #our left and right ptrs won't cross they will just land on each other at the end
        while left < right: 
            mid = (left + right) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1 
            elif nums[mid] < nums[-1]:
                right = mid
            elif nums[mid] < nums[-1] and nums[mid] > nums[0]:
                return nums[0]

        return nums[left]

