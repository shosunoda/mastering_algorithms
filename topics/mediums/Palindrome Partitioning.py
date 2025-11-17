from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # so i mean we ahve to try and split into palndromes 
        # that means we can split a string if it is a plaindrome
        # so let us do that
        result = []
        def isPalindrome(palindrome):
            return palindrome == palindrome[::-1]
        def dfs(index, path):
            if index == len(s):
                result.append(path[:])
                return
            for ending in range(index + 1, len(s) + 1):
                if isPalindrome(s[index: ending]):
                    path.append(s[index:ending])
                    dfs(ending, path)
                    path.pop()
            return
        dfs(0, [])
        return result
        

        