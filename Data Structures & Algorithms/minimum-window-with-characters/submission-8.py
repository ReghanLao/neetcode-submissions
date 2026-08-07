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
        Let's use the notion of have and need to guide us to solve this problem. have and need don't track total 
        character counts - they track how many DISTINCT characters are 
        currently "satisfied" in our window and the number of distinct characters we need to fulfill respectively

        need_counts tells us, for each character in t, how many copies we require.
        need is simply the number of distinct characters in t - i.e. len(need_counts) 

        have_counts tells us, for each character we care about, how many copies are currently in our window.
        have is the number of distinct characters whose count in have_counts has reached (exactly matches) 
        the count required in need_counts. 
        
        have only goes up when a character's count TRANSITIONS to being 
        exactly satisfied, and only goes down when a satisfied character's count drops below what's required.

        Once have == need, every distinct character t needs is present in sufficient quantity - the window 
        is valid. We capture this as a potential solution, updating res if it's shorter than our historical 
        minimum. Then we shrink the window from the left to look for a smaller valid window, updating have 
        accordingly if shrinking causes a previously-satisfied character to fall short again.

        We keep two dictionaries: one for the counts we need (from t), and one for the counts we currently 
        have in our window (only tracking characters that appear in t).
    '''
    def minWindow(self, s: str, t: str) -> str:
        #track best indicies and then splice at the end 
        best_indicies = [0,0]
        best_len = math.inf

        #for both dicts we will only store characters from t as keys 
        need_counts = Counter(t)
        have_counts = defaultdict(int)

        left = 0 

        #required to check if we have what we need
        have = 0 
        need = 0

        #the number of distinct characters that are needed 
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
                if ((right - left + 1) < best_len):
                    best_indicies = [left, right]
                    best_len = min(best_len, right - left +1)
                
                #shrink window by moving left & update the counts of have accordingly if applicable 
                if s[left] in have_counts:
                    have_counts[s[left]] -= 1

                #if we remove what we have at left and it falls under what we need - update what we have all in all if its a character we care about after all
                if s[left] in have_counts and have_counts[s[left]] < need_counts[s[left]]:
                    have -= 1

                left += 1
            
        if best_len != math.inf:
            best_left, best_right = best_indicies        
            return s[best_left:best_right + 1]
        else:
            return ""
            
            


                