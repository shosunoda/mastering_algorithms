from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #["2","1","+","3","*"]
        # this is 2 + 1, * 3
        # ["4","13","5","/","+"]
        # 4, + 2 = 6
        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # 10, 6, 9,,3 
        # 10,6, 12, -11, 
        #, 10, 6, -132, 
        # 10, -22
        # stack, whenevwe e encounter a number, wee just add it to our stack
        # if we ever encounter an operation, we should pop the lastw two elements on the stack
        # do the operation, with the firt operand being the first opersand, 
        # and that towards the stack
        #
        #
        stack = []
        for item in tokens:
            if item.isdigit():
                stack.append(int(item))
            elif len(item) > 1 and item[0] == "-" and item[1:].isdigit():
                stack.append(- int(item[1:]))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                if item == "+":
                    stack.append(first_operand + second_operand)
                elif item == "-":
                    stack.append(first_operand - second_operand)
                elif item == "/":
                    stack.append(int( first_operand / second_operand))
                elif item == "*":
                    stack.append(first_operand * second_operand)
        return sum(stack)

        