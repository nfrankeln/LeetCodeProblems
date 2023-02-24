class Solution:
    def isValid(self, s: str) -> bool:
        mirror = {"(": ")", "{":"}", "[": "]" }
        stack = []
        for char in s:
            # if char is a left-hand image add to stack
            if char in mirror:
                stack.append(char)
            #if its a right handed image check if list is empty 
            elif not stack:
                return False
            #if not empty check if it matches the last char on the stack
            # if it matches then remove top of stack
            elif mirror[stack[-1]] == char:
                stack.pop()
            else: 
                return False
            # if we get to end of the input make sure our stack is empty
        if stack:
            return False
        else:
            return True
            