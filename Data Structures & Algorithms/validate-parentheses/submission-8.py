class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Basically we need to match every single 
            
            Open Bracket with the same type of close bracket 
            in the same order 

            If this can be done we have a valid input string 

            Lets match every close bracket with the latest 
            open bracket we have seen. If they are of the same type
            then so far we have a valid string if not then this 
            string is not valid 

            To faciltate this above process it is suitable for us to 
            keep track of the open brackets in LAST IN FIRST OUT manner
            because we want to match the most recent open bracket we've 
            seen to the close bracket we are iterating over
        '''

        stack = []

        for bracket in s:
            #take open bracket and add them to the list of open brackets 
            #we have 
            #most recently seen so we can check them against the
            #close brackets we are iterating over 
            if bracket in ['[', "{", "("]:
                stack.append(bracket)
            else:
                #check if there even is a corresponding open bracket
                #for this close bracket bc what if we start 
                #with an open bracket 
                if stack:
                    open_bracket = stack[-1]
                    close_bracket = bracket

                    #we are able to match a pair of parentheses so 
                    #we remove this pair from further consideration
                    if open_bracket == "[" and close_bracket == "]":
                        stack.pop()
                    elif open_bracket == "{" and close_bracket == "}":
                        stack.pop()
                    elif open_bracket == "(" and close_bracket == ")":
                        stack.pop()
                    #this pair is not the same type so we return false 
                    else:
                        return False
                else:
                    return False

        #if we are able to match every pair of parentheses then our
        #stack should be empty 
        return len(stack) == 0 
        