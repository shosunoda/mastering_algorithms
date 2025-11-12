from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]


        start = 0
        end = 0
        max_str = s[0]

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1) 

            
            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        
        return max_str