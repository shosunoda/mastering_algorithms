from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # is this not sliding window, 
        # lets try scan this, abca,, bcab, cabc, cbb
        left = 0 
        frequency_map = defaultdict(int)
        longest = 0
        for right in range(len(s)):
            frequency_map[s[right]] += 1
            while left < right and frequency_map[s[right]] > 1:
                frequency_map[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
    
            

        