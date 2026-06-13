import math 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = math.inf

        for s in strs:
            min_length = min(len(s), min_length)
        
        #the longest common prefix is bounded by the shortest string
        #the longest common prefix is at most as long as the shortest string
        #a common index iterating thru every single string at the same 
        #position 
        index = 0

        while index < min_length:
            for s in strs:
                #if the char at the current string is not equal to 
                #the char at any other given string then this isn't a common
                #prefix return the longest common prefix up to here
                if s[index] != strs[0][index]:
                    return s[:index]
            index += 1
        
        return strs[0][:index] 
        
        