import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        window, countT = {}, {}
        left = 0 
        have, need = 0, 0
        res, resLen = [-1, -1], math.inf

        for i in range(len(t)):
            char = t[i]
            countT[char] = countT.get(char, 0) + 1
        
        need = len(countT)

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # we have just satisfied a condition 
            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                #we have a potential solution but we also need 
                # to shrink window  

                #we have a better solution than before 
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                #pop from the left of our window to shrink window 
                #after we pop from left it is possible that we no longer
                #have what we need 
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        final_left, final_right = res
        return s[final_left : final_right+1] if resLen != math.inf else ""
        




