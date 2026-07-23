class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            We can tackle this in a brute force manner obviously 
            by evaluating our possible triples st i, j, k are distinct 
            but this performs a lot of unnecessary work 

            Instead of performing unnecessary work we should be seeing
            how our sum compares to our target and allign our search space
            accordingly 

            What does this mean?

            If we sort the input array and have three ptrs i, j, k -
            we can take the sum at these ptrs and compare that sum
            to our target sum of 0. 

            We then can shift our ptrs accordingly to get closer to our
            target sum of 0. If our current sum is too little shift up
            and if our sum is large them shift down.

            Lets implemement this idea by
            fixing a ptr i at an element and have this
            step thru every element in the array once. 
            
            We then want to fix
            two other ptrs: j and k and these will be the ptrs we shift
            up or down according to how the sum derived from summing the
            the nums at these three ptrs compare to the target sum

            j and k will start after i at the respective ends of the subarray
            produced after i
        '''
        #sorting nums will allows to properly adjust our ptrs accordingly
        #moving our ptrs in the desired direction (increase in sum or decrease in sum)
        nums.sort()

        #[-4, -1, -1, -1, 0, 1, 2, 2].

        res = []
        target = 0

        
        for i in range(len(nums)):
            #if we land on a duplicated starting value we run the risk
            #of producing duplicate triplets which we dont want
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1

                    #if we find solution and our inner ptrs land on
                    #the same number as it was previous
                    #we basically produce a dup triplet which we dont want
                    while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                        j += 1

                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1
                    
                elif curr_sum > target:
                    k -= 1
                else:
                    j += 1
            
        return res 
            

