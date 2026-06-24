class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Notice that our input is constrained to only the lowercase
            English letters

            Instead of sorting the strings for the anagrams to have a common key
            in the hashmap 

            Since we know we are confined to only 26 letters we can use an 
            array of size 26 as our common key and let each index represent
            a character as we go through each character in each word and count
            how many times it occurs

            Every anagram will have a common array if we do it like this

            Going from sorting to counting 

            Our time complexity goes to n * m, for every word
            we are just counting m characters 
        '''

        groups = defaultdict(list)
        #going through every single word
        for word in strs:
            count = [0] * 26
            #and go through every single one of its characters and count 
            #how many times each character is present 
            for char in word:
                #this subtraction automatically maps to the indicies of the array
                count[ord(char) - ord('a')] += 1
            
            #the count array is now or common key that can group tg anagrams
            groups[tuple(count)].append(word)

        res = []
        for _, val in groups.items():
            res.append(val)

        return res