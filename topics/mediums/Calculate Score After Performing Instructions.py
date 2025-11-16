from typing import List
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        # we just have to go through both arrays at the same time
        # as as go through them, we check what the insturtion, 
        # if its addition insturction, we can go to the next instruction  and add the score to our current total
        # if its a jump insturction, we can jump to according insutiction
        # and we have base cases of visiting beyond the end of the array 
        # and also reivisiting an already existing insutrction
        # so this is very much dfs/recursion, 
        # we have to keep track of what steps have been seen, the overallscore, and yeah that should be i
        visited = set()
        processed_list = list(zip(instructions, values))

        def dfs(index):
            if index < 0 or index >= len(instructions):
                return 0
            if index in visited:
                return 0 
            instruction, value = processed_list[index]
            visited.add(index)
            if instruction == "add":
                return value + dfs(index + 1)
            else:
                return dfs(index + value)

        return dfs(0)
            
        