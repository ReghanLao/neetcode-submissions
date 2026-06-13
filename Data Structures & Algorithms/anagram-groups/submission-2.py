from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagrams when sorted are the same word
        groups = defaultdict(list)
        res = []

        for word in strs:
            sorted_key = "".join(sorted(word))
            groups[sorted_key].append(word)

        for k, v in groups.items():
            res.append(v)
        
        return res