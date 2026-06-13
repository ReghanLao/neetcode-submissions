from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Boyer moore approach 
        #we want to reduce the space complexity to O(1) therefore 
        #lets just hold the two most frequent elements in the hashmap
        #we can have at most two most frequent elemenets when finding elements 
        #that appear more than a third of a time 

        counts = defaultdict(int)

        for num in nums: 
            counts[num] += 1

            #if the length of our dict/hashmap exceeds two then
            #lets decrement the count of every element because
            #survival of the fittest -> we gradually eliminate weaker candidates
            #strongest candidate(s) will come out on top naturally 
            if len(counts) > 2:
                #decrement count of every element
                for n, c in counts.items():
                    counts[n] -= 1
                
                #remove element from dict if it has been eliminated (count is 0)
                #aka add elements to new dict if count not 0 
                new_dict = defaultdict(int)
                for n, c in counts.items():
                    if counts[n] > 0:
                        new_dict[n] = counts[n]

                counts = new_dict
            
        print(counts)
        res = []
        #verify remaining candidates are majority element (appear more than a third of the time)
        for num in counts:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res