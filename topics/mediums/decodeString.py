class Solution:
    def decodeString(self, s: str) -> str:
        # i mean this is very clearly d fs problem cause everytime we encounter a nested loop 
        # we want to process those first right 
        # with dfs, it usually comes with stack 
        # beacuse a stack allows to pop things in lifo, which is how dfs traverses layers
        # now, how would we represent this on a stacl 
        # "3[a2[c]]"
        # [3, [, a ,2, c, ], ] ]
        # lets go through it, we see a s3, we see an opening bracket, we see a , and then we see a 2 
        # at this point we shouldnt process anyting yet cause we havent fully process it due to not enocuntering the closing bracket
        # so lets go deeper again
        # we see a another [, c ], and then we see the closing bracket, this is when should 
        # process a bracket right
        # we can look back, 
        # and then we can add the string back 
        # until we encounter the opening bracket
        # and then there, we will encounter digit where we have to rpces things again
        # 
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                counter = ""
                while stack and stack[-1].isdigit():
                    counter = stack.pop() + counter
                stack.append(int(counter) * substring)
        return "".join(stack)

        