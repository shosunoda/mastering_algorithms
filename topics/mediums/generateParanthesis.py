from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we are given n pairs of parenthesis
        # which means we have n left parantehsis and n right paraneheis
        # lets carefully efine what a valid forme dparatneshsi
        # it just means that for every right parantehsis, there is at least one left parantehsis to the left of it
        # this means that you cannot add right paratenehss if you don't have enough left paratneshs
        # given this rule, we can code this reucrsively of through backtrackign maube 
        # this can be done through backtgrackign cause everytime we explore a full on decision tree
        # we can just pop a path, and traverse the other potential paths, we could have explored?
        #every point in the decision tree is defined by how many left paranteshsi, and how many right paratneshs
        # when we each n - left = right, thats our base case, whwere add the path 
        # how do explore different paths
        # so when have more left parenthesis than right paranhesis, we can choose two optiosn
        # which is to add a right paranthesis, and to choose a left paretneshs if we have less than parnrhtesis 
        # if we have the same amount of parantehsises, 
        # we can only add left 
        # the one thing i haven't fully scoped is how to explore the other paths 
        #
        result = []
        def bracketTraversal(left, right, path):
            if left == right == n:
                result.append("".join(path))
            if left > n or right > n:
                return
            path.append("(")
            bracketTraversal(left + 1, right, path)
            path.pop()
            if left > right:
                path.append(")")
                bracketTraversal(left, right + 1, path)
                path.pop()
            return 

        bracketTraversal(0,0, [])
        return result
        