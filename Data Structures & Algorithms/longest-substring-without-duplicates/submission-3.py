class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window -> ensure that window doesn't have any duplicate characters 
        #we can keep a set for the elements we have seen in the current window to check for dups

        left = 0 
        seen = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in seen: 
                #shrinking the bounds of our window from the start 
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest 
