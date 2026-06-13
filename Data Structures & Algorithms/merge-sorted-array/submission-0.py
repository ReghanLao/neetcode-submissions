class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged = []
        left = 0 
        right = 0

        while left < m and right < n:
            if nums1[left] < nums2[right]:
                merged.append(nums1[left])
                left += 1
            else:
                merged.append(nums2[right])
                right += 1
        
        #fill in the remaining elements in non exhausted array
        #either one of these will run
        while left < m:
            merged.append(nums1[left])
            left += 1

        while right < n:
            merged.append(nums2[right])
            right += 1
        
        #now merge is completely populated in non decreasing order

        for i in range(len(nums1)):
            nums1[i] = merged[i]
