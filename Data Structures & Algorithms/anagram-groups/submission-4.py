class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagrams are words that have the same characters and the same
        #number of those characters 

        #we can go through every single string and
        #and map it to the sorted version of it  
        #this will naturally group anagrams together 

        #key: sorted string 
        #value: anagrams associated with sorted string
        mapping = defaultdict(list)

        for word in strs:
            sorted_string = "".join(sorted(word))
            mapping[sorted_string].append(word)

        res = []
        for key, val in mapping.items():
            res.append(val)

        return res