class Solution:
    def countDistinct(self, n: int) -> int:
        # 223 
        # 10, 20, 30 , 40 , 50 , 60, 70, 80, 90, 100, 110,
        #91, 92, 93, 94, 95, 96, 97, 98 ,99, 100, 101 
        # 100 and 200,
        s = str(n)
        length = len(s)

        pow9 = [1] * (length + 1)
        for i in range(1, length + 1):
            pow9[i] = pow9[i-1] * 9
        
        result = 0
        for d in range(1, length):
            result += pow9[d]

        for i, ch in enumerate(s):
            digit = int(ch)
            if digit == 0:
                return result
            result += (digit - 1) * pow9[length - i - 1]

        return result + 1