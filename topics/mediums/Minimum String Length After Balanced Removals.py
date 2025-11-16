class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a_length = sum([1 for char in s if char == 'a'])
        b_length = sum([1 for char in s if char == 'b'])
        return len(s) - 2 *min(a_length, b_length)
        