class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tuple_set = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet_sorted = tuple(sorted(triplet))
                        tuple_set.add(triplet_sorted)

        res = []
        for item in tuple_set:
            res.append(list(item))

        return res



