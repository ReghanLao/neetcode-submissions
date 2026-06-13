class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurences = set()
        left = 0
        right = 0 
        max_length = 0
        n = len(s)

        for right in range(n):
            while(s[right] in occurences):
                occurences.remove(s[left])
                left += 1
            
            occurences.add(s[right])
            
            curr_length = (right - left) + 1

            max_length = max(curr_length, max_length)

        return max_length 
            

