class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # 
        # 
        count = 0
        for subword in patterns:
            if subword in word:
                count += 1
        return count
        