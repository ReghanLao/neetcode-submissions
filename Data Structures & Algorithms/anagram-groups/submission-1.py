class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
         
        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            
            groups[tuple(count)].append(word)
        
        return list(groups.values())