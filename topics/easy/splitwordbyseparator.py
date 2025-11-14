from typing import List
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = [word.split(separator) for word in words]
        output = []
        for potential in result:
            for word in potential:
                if word:
                    output.append(word)
        return output
        