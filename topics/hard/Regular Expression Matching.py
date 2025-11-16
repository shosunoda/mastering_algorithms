class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # what does thie require, it requires us to save the previous character
        # thats about it no?
        # we go through the string
        # if we encounter a "." then we can accept any string
        # we save this and use this for the next element 
        # look like a relatively simple dfs
        # if we reach the last index, we return TRue
        # if at any scenario we can't match the string, we should return False
        # 
        cache = {}
        
        def dfs(s_index, p_index):
            if p_index == len(p):
                return s_index == len(s)
            
            if (s_index, p_index) in cache:
                return cache[(s_index, p_index)]
            
            first_match = s_index < len(s) and (p[p_index] == s[s_index] or p[p_index] == '.')
            
            if p_index + 1 < len(p) and p[p_index + 1] == '*':
                result = (dfs(s_index, p_index + 2) or  
                         (first_match and dfs(s_index + 1, p_index)))  
            else:
                result = first_match and dfs(s_index + 1, p_index + 1)
            
            cache[(s_index, p_index)] = result
            return result
        
        return dfs(0, 0)