class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        #will keep track of a character and its freq in
        #the current window 
        char_freq = {}
        n = len(s)
        max_length = 1

        for right in range(n):
            # expand window 
            if s[right] in char_freq:
                char_freq[s[right]] += 1
            else: 
                char_freq[s[right]] = 1

            # checking and shrinking the window if and
            # while # of replacements 
            # exceed k
            while (right - left + 1) - max(char_freq.values()) > k:
                char_freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
        



            

