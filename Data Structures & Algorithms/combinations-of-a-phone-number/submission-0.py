class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        When building a combination at any given point in time each digit maps to any one of its possible characters but ONLY one - this is how we building the combinations 

        For every character than a digit maps to we want to append every character that the next digit maps to and so on and so forth 

        We want all possible combinations so lets choose -> recurse -> backtrack

        We are able to backtrack and visit all possible combinations because our digits length is relatively small <= 4
        '''

        #first need to map digit to list of characters it can rep
        phone = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'], 
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
        }

        #hold all possible letter combinations that digits could represent 
        res = []

        if len(digits) == 0:
            return []

        #i represents the ith digit we are iterating over at a current time 
        #candidate represents the current letter combination we have built 
        def backtrack(i, candidate):
            #make sure our candidate sol isnt empty so we don't append empty string to res 
            if len(candidate) == len(digits):
                res.append("".join(candidate.copy()))
                return 
            
            #we can start building our possible letter combinations from any start char that the digit maps to 
            for char in phone[digits[i]]:
                candidate.append(char)

                #go to the next digit to continue building this combo chain
                backtrack(i + 1, candidate)

                #backtrack by removing the character just chosen
                candidate.pop()

                #for loop visits the next branch for us 
        backtrack(0, [])
        return res