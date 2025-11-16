class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        rev = s[::-1] if s[0] != '-' else s[:0:-1]
        
        rev_int = int(rev) if x >= 0 else -int(rev)

        if rev_int < -2**31 or rev_int > 2**31 - 1:
            return 0

        return rev_int