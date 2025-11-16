class Solution:
    def distMoney(self, money: int, children: int) -> int:
        #
        if children > money:
            return - 1
        #we want to maximise money such that no chilren gets 4 dollars, but every children must receive 1 dollar 
        # 20 - 3 = 17
        # 17 // 7
        # however,  is the modulus of this is 3
        # we are given the rule everyone msut receive one dollar
        # so we can subtract the amount we have left by children
        # now the rule is that how many children can we have 7 dollars, and not 3 dollars
        # and we must all ouf money 
        # the most amount of 7s we can give out is amount)left // 7, 
        # if the number of childrne is greater than that, and the remainder isnt 3, then we acn distribuet the maximum
        # if the childrne is less than that, we can only distribute to cihldren - 1, and give one perosn the maxium amount
        # if number of children is greater than, and the remainder is 3, then we also distribute maximum -1 
        if money < children:
            return -1

        money -= children

        remain = min(money // 7, children)

        money -= 7 * remain

        remainingChildren = children - remain
        
        if remainingChildren == 1 and money == 3:
            remain -= 1
        elif remainingChildren == 0 and money > 0:
            remain -= 1
        return remain