class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.frequency_map(s) == self.frequency_map(t)
        
    def frequency_map(self, word):
        frequency_map = [0]* 26
        for char in word:
            frequency_map[ord(char) - ord('a')] += 1
        return tuple(frequency_map)
        