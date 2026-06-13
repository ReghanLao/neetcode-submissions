class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram -> word with same character frequencies -> use hashmap 

        return Counter(s) == Counter(t)