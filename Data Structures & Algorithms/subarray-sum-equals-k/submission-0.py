from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        curr_prefix_sum = 0
        count = 0 

        prefix_sums[0] = 1

        for num in nums:
            curr_prefix_sum += num
            if curr_prefix_sum - k in prefix_sums:
                count += prefix_sums[curr_prefix_sum - k]
            prefix_sums[curr_prefix_sum] += 1

        return count 
