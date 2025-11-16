from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # so apparently the opimum choice is here to buy 0, sell3, buy 1, sell 4
        # this is different from the optimium for one purchase which is to buy 0, sell 4
        # why is it different 
        #clearly, we cant treat these two purchases as independent 
        # we must take them into account somehoe 
        # i think this is very clearly dynamic programming
        # with like 4 variales or something
        # it would be index, bought index, purchases_ left and this would correspond to a total of somethign 
        # [index][bought_index][purchases_left] = 
        # max([index + 1][-1][ purchases_left -1] + bought - sold 
        # max([index + 1][bought_index][ purchases_left])
        # and then theres two alternate choics if we havent boght so yeah
        cache = {}
        def dfs(index, holding, transactions_left):
            if index == len(prices):
                return 0
            
            if (index, holding, transactions_left) in cache:
                return cache[(index, holding, transactions_left)]
            
            do_nothing = dfs(index + 1, holding, transactions_left)
            
            if holding:
                sell = prices[index] + dfs(index + 1, False, transactions_left - 1)
                result = max(do_nothing, sell)
            else:
                if transactions_left > 0:
                    buy = -prices[index] + dfs(index + 1, True, transactions_left)
                    result = max(do_nothing, buy)
                else:
                    result = do_nothing

            cache[(index, holding, transactions_left)] = result
            return result
        
        return dfs(0, False, k)

                
                


        