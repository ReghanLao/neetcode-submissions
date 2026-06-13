import math 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT = {}
        window = {}
        left = 0 

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        have = 0
        need = len(countT)
        
        res = [-1, -1]
        resLen = math.inf

        #sliding a window over s
        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if right - left + 1 < resLen:
                    #we have a better solution
                    res = [left, right]
                    resLen = right - left + 1

                #need to shrink window to find more potential sol
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        #we may now have a substring that meets the conditions
        left, right = res

        return s[left:right + 1] if resLen != math.inf else ""


