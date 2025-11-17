from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we want to return the widnow in which every character in t is included
        # edge cases if t is larger than s then its impossible, we return the empty string
        # also judhing from how this question is asked
        # it seems like very standard sliding window problem 
        # and the window we have to maintain at all times is minimum size of t 
        # this is going go be dynamically shifting window
        # we need to define a few subprioblems in this question I think
        # in what condition, do increase/decrease window size
        # how we determine a match 
        # we determine a mtatch, when freuqnecy_map of t is all zero
        # this one is a bit tricky but very doable to do 
        # my main question is how do we decide when to increase/decrease the dinwo size
        # we only ever discard from the left if we can find another amtch in the right side of the window
        # this decision can be rationalised by how to find a match a palce in the first place, you need a that character
        # so unless you find a anther match, this is the only window 
        # which means once you find a decreased window you can 

        if len(t) > len(s):
            return ""
        tmap = defaultdict(int)
        for char in t:
            tmap[char] += 1
        distinct = len(tmap)
        formed = 0
        s_window = defaultdict(int)
        left = 0
        min_length, result = float('inf'), [-1, -1]

        for right in range(len(s)):
            char = s[right]
            s_window[char] += 1
            if char in tmap and s_window[char] == tmap[char]:
                formed += 1
                while left <= right and formed == distinct:
                    if (right - left + 1) < min_length:
                        min_length = (right - left + 1)
                        result = [left, right]
                    removed = s[left]
                    s_window[removed] -= 1
                    left += 1
                    if removed in tmap and s_window[removed] < tmap[removed]:
                        formed -= 1
        return "" if min_length == float('inf') else s[result[0]:result[1]+1]


