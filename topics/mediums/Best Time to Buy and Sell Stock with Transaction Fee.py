from typing import List 
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # so our usual stock diagram can be diagramed like this right
        # 3 + 4
        # 5
        # 7 -2 = 5
        # 9 -4 -2 = 3
        # = 8
        # as we can saw in this example, there are consquences in attempting to multple transactions 
        # because costs scale with # of transactiosn
        # and in the usual stock market 
        # the amount gained between 4 and 1, and 8 and 4 would be the same as a8 and 1 rigt
        # but this time its not the due transaction fee
        # because we don't actually know if its the best transaction until we look at the future
        # dp is probably a good choice for exploirng potentual paths 
        # we could have 2 variables, which is index, and golding i guess
        #
        #
        #                   9
        #       8
        #           4
        #  4        
        #.   
        #1
        cache = {}
        def dfs(index, holding):
            if index >= len(prices):
                return 0 
            cachekey = (index, holding)
            if cachekey in cache:
                return cache[cachekey]
            if holding:
                sellnow = -fee + prices[index] + dfs(index + 1, not holding)
                selllater = dfs(index + 1, holding)
                cache[cachekey] = max(sellnow, selllater)
                return cache[cachekey]

            else:
                buynow = -prices[index] + dfs(index + 1, not holding)
                buylater = dfs(index + 1, holding)
                cache[cachekey] = max(buynow, buylater)
                return cache[cachekey]
        return dfs(0, False)

        