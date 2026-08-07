from collections import Counter, defaultdict 
class Solution:
    '''
        We basically want to return the shortest substring s that contains all characters in t 
        
        Brute Force:
        We can brute force solve this by iterating over every single possible substring and seeing if the substring contains all the letters in t - basically t being a subset of this substring. If this is possible, then note this and return the shortest possible substring where t is basically a subset of the substring

        This may be problematic because we need to potentially iterate through substrings
        that never contain the characters present in t which will cause us to perform
        unnecessary work. 

        Sliding Window Approach:
        Instead of evaluating every single substring what if we just slide a window over this string and count the characters as we go.

        If we find a substring with all of t's characters we want to note this and shrink our current window until our current substring doesn't have all of t's characters anymore 

        We constantly update our res string if we find a better shorter string 

        Neetcode Solution:
        Let use the notion of have and need to guide us to solve this problem. The current substring that we are looking at
        has x amount of characters but lets say it needs y amount of characters. 

        We have a total numebr of characters that we have at any given time and total of number characters that we need

        Lets say we have 1 character -> a
        Lets say we all in all need 3 characters -> a, b, c

        have will be 1 and need will be 2 

        We only update have if in our window the specific character 
        and its count alligns with need's character and its required count 

        Once we have what we need we can capture this as a potential solution and store it - we want to store the minimum
        so update our result variable if its shorter than our historial result 

        After we capture our potential solution we want to capture more potential solutions so shrink our window and remove
        characters from the left of our window. we update have accordingly if we lose a character and it falls under the need 
        count.

        we will have a dictionary that keeps track of the count of our need and another dictionary that will keep track of the 
        count that we have 
    '''
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        #for both dicts we will only store characters from t as keys 
        need_counts = Counter(t)
        have_counts = defaultdict(int)

        left = 0 

        #required to check if we have what we need
        have = 0 
        need = 0

        need = len(need_counts)
      
        for right in range(len(s)):
            #we only care about tracking the counts of the characters we care about aka the characters in t for our current substring / window
            if s[right] in need_counts:
                have_counts[s[right]] += 1
            
                #if we have what we need for this character update our all in all have count
                if have_counts[s[right]] == need_counts[s[right]]:
                    have += 1
            
            #we have landed on a potential solution

            while have == need:
                #if we haven't set our res before or this current solution is better than our historial minimum
                if res == "" or ((right - left + 1) < len(res)):
                    res = s[left:right + 1]
                
                #shrink window by moving left & update the counts of have accordingly if applicable 
                if s[left] in have_counts:
                    have_counts[s[left]] -= 1

                #if we remove what we have at left and it falls under what we need - update what we have all in all if its a character we care about after all
                if s[left] in have_counts and have_counts[s[left]] < need_counts[s[left]]:
                    have -= 1

                left += 1
            

            
        return res
            
            


                