class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_length = 1
        n = len(s)

        for right in range(n):
            counts[s[right]] = counts.get(s[right], 0) + 1

            #while the num of chars we have to replace is more than k then our window is invalid and 
            #we must shift our window to check for other substring candidates
            while right - left + 1 - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        
        return max_length