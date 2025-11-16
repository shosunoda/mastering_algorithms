from collections import defaultdict
from typing import List, Dict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # an anagram is defined as being able to form a different letters of a word using the letters of an original one
        # so nat, ant, tan ar all anagrams
        # so we realise we don't actually care about the order of these elements
        # and thus,what we realise is that groups of anagrams can be identiefed by their frequency_lists
        # so what if attempt to use frquency_lists as kaeys
        # meaning if that if two words have a the same frequency_list, the index into the same bucket, and thus we can add the words there
        # two wrods having the same freuqqncy_list means they are angrams of each other 
        # so the problem here comes into how bwest to compute a frequency_list
        #we are told that it consists of loweercase letters 
        # and python has a pretty handy built in fucntion that allows for us to do soemthing like this 
        # which is to convert characters into integers 
        # and since theres 26 letters in the alphabet, a frquency list can be defined as a array of 26 indexes with each idnex correspodning to a lettet 
        # lets try and do this 
        frequency_group: Dict[List[int], List[str]] = defaultdict(list)
        for word in strs:
            frequency_map = [0] * 26
            for char in word:
                frequency_map[ord(char) - ord('a')] += 1
            frequency_group[tuple(frequency_map)].append(word)
        result = []
        for key, value in frequency_group.items():
            result.append(value)
        return result
        