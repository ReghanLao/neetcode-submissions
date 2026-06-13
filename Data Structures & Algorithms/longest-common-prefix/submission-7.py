import math 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #basically the idea is to iterate through every word in parallel
        #check the characters at the current parallel iteration and see
        #if they are the same if so this continues the common prefix and if
        #not then this ends the common prefix 

        #but note during parallel iteration we can only iterate up to the 
        #length of the shortest word

        res = ''
        min_length = math.inf

        #shortest word's chars will be used as an anchor in parallel iteration to compare to other word's char to see if a common prefix exists or not
        shortest_word = ''
        for word in strs:
            if len(word) < min_length:
                min_length = len(word)
                shortest_word = word 
        
        #now we can act start iterating over every word in parallel up to min length
        #for a valid common index check all words in parallel if they form a common prefix or nto 
        for i in range(min_length):
            for words in strs: 
                if words[i] != shortest_word[i]:
                    return res 
            res += shortest_word[i]
        
        return res
