class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # #
        # so there are like kinda 2 contrains here, 
        # so one is for city1, and city2, there needs to be people on each 
        # and like theres a choice for each tuple, you can only choose option1 provided you dont choopse option 2
        # and then we want to minimise this total cost 
        # 
        #
        # [[10,20],[30,200],[400,50],[30,20]]
        # lets do this, 
        #  lets take 10, lets do 30, and then we do 50, 20 
        # the point is we need to first sort it right,, and then see what we want to do from there 
        # we need some lgoic to somehowo determine when to choose option a 
        #[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        # a, b, b, b, b, b
        # right, sot ehres a limit here, so we have to figure out given that we have n choices, 
        # which one to choose for optoin a and option b whilst keeping glibal cost down 
        # 
        # so for each tuple, we obiously have to choose soemthing right
        # so we want to choose the one that would cur the least cost, that can be coded through the absolute value difference 
        # as that would indicate the priority on the global cost scale 
        #
        costs.sort(key = lambda x: abs(x[1] - x[0]))
        costs.reverse()
        cost = 0 
        city1 = 0 
        city2 = 0
        n = len(costs) // 2
        for costa, costb in costs:
            if costa < costb:
                if city1 == n:
                    city2 += 1
                    cost += costb
                else:
                    city1 += 1
                    cost += costa
            else:
                if city2 == n:
                    city1 += 1
                    cost += costa
                else:
                    city2 += 1
                    cost += costb
        return cost


        