class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        need_length = len(needle)
        if needle == haystack:
            return 0
        for index in range(len(haystack) - need_length + 1):
            if haystack[index:index + need_length] == needle:
                return index
        return -1
        