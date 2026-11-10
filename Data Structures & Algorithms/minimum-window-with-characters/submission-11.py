from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        we want the shortest substring of s where every char in t is included
        even dups 

        constraints:
        t might not exist -> ""
        s and t not empty 
        s and t consists of uppercase and lowercase english chars 

        brute force: eval all possible substrings to see if they contain t

        better: slide a window over s, see if we have what we need, we only can increment our have counter if the char coming into the window is in t and the have count for that particular char is the same as t's, if we have what we need if have == need store the length of candidate substr and store their indicies, shrink our window from the left and only update the chars counts taht matter aka if we shrink our window and its in our have dict already we can update the value associated with that char, while we have what we need compute an answer basically
        '''

        have = need = 0 
        have_counts = defaultdict(int)
        need_counts = defaultdict(int)

        for char in t:
            need_counts[char] += 1
        
        need = len(need_counts)

        left = 0

        res_ind = [-1,-1]
        res_len = float('inf')
        
        for right in range(len(s)):
            if s[right] in need_counts:
                have_counts[s[right]] += 1

                if have_counts[s[right]] == need_counts[s[right]]:
                    have += 1 
            
            #we can compute the candidate answer 
            while have == need:
                curr_len = right - left + 1
                if curr_len < res_len:
                    res_len = min(res_len, curr_len)
                    res_ind = [left, right]

                #shrink our window to find shorter substrings of s that
                #contain every char in t 
                if s[left] in have_counts:
                    have_counts[s[left]] -= 1

                    if have_counts[s[left]] < need_counts[s[left]]:
                        have -= 1

                left += 1
        
        if res_len == float('inf'):
            return ""
        left, right = res_ind[0], res_ind[1]
        return s[left: right + 1]
        




