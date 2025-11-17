from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        # everytime we see a left paranthesis, we know there needs to be a right paranthesis
        # this applies to all types of left prarantehsis
        # if we see a right partenhesis even thought we shonlt have any right parantehsis, it becoems invalid
        # and the end of processing, the stack should be empty
        leftbrackets = set(["(", "{", "["])
        rightbrackets = set([")", "}", "]"])
        left_to_right = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in leftbrackets:
                stack.append(left_to_right[char])
            elif char in rightbrackets:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False
        return not(stack)
