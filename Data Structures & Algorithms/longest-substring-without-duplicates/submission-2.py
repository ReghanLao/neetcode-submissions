class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        max_length = 0

        #left to i defines a current valid window 
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])

            max_length = max(max_length, i - left + 1)

        return max_length


            