from collections import defaultdict 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #as we iterate throught the string we want to maintain a window
        #maintaining a window emulates the creation of subtrings and enforces this sense of continuity which is required of a subtring
        #in every single one of our windows/substrings we want to ask
        #1) what is the most frequently occuring character here
        #2) how many times do I need to perform character replacements for characters to match the most frequently occuring character 
        #3) is that number less than or equal to the number of replacements we are allotted if so then lets compute the length of this substring as if we made that replacement 
        #4) if not then lets start a new window/substring starting from where we were invalidated 

        left = 0
        max_len = 0 
        occur = defaultdict(int)

        for right in range(0, len(s)):
            occur[s[right]] += 1

            replacements = (right - left + 1) - max(occur.values())

            while replacements > k:
                occur[s[left]] -= 1
                left += 1 
                replacements = (right - left + 1) - max(occur.values())

            max_len = max(right - left + 1, max_len)


        return max_len


