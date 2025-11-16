from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #so the thing with this you realise that you have to rpcess thiese seuqneitally
        # in as if i have le leet code et 
        # and my word dictionary was leet code and 
        # i cant leet code 
        # leet, and say its true
        # so a hint is that we have to rpocess this sequentially
        # and because of this, we need a way to check if the first whatever characters match any of those words in the 
        # dictionary 
        #if it does, we can continue onwards
        # also the thing is, there are multiple possible pahts, wand we dont actually realise until the end if its true or not
        # appplespenapple and our ductionary was apple, apples plen
        # if we use apple at the beginning, we cant actually finish it cause, but if we use apples, we can 
        # this hints to me that we have to use dp to pursue different subpobrlems which is dependent on the index of the word 
        # so each subprobelm can be deinfed as through the index we are at
        
        # the problem is that we need two functions, one to travel through the dp array
        # and another to match the words within the array 
        #
        wordset = set(wordDict)
        cache = {}
        def dfs(index):
            if index == len(s):
                return True
            if index in cache:
                return cache[index]
            
            for end in range(index, len(s) + 1):
                if s[index: end] in wordset:
                    print(index, end)
                    if dfs(end):
                        cache[index] = True
                        return True
            cache[index] = False
            return False
                    
        return dfs(0)
        