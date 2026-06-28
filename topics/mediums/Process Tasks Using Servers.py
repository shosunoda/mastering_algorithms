from heapq import heapify, heappush, heappop 
from collections import deque
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        #  we are given two arrays, servers and tasks of length 
        #  n and m respectively 
        #  servers[i] is the weight of the ith server, and tasks[j] is the time neede
        #  to process the jth task 
        #  tasks are assigned to server using a queue 
        tasks_queue = []
        server_queue = []
        for index, server_weight in enumerate(servers):
            heappush(server_queue, (server_weight, index))
        time = 0 
        answer = [-1]* len(tasks)
        # task queue will have tiem and server

        for task_index, task_duration in enumerate(tasks):
            time = max(time, task_index)
            while tasks_queue and tasks_queue[0][0] <= time:
                released_time, free_server = heappop(tasks_queue)
                heappush(server_queue, (servers[free_server], free_server))
            
            if not server_queue:
                time = tasks_queue[0][0]
                while tasks_queue and tasks_queue[0][0] <= time:
                    released_time, free_server = heappop(tasks_queue)
                    heappush(server_queue, (servers[free_server], free_server))
            #  assign servers 
            free_weight, free_index = heappop(server_queue)
            answer[task_index] = free_index
            heappush(tasks_queue, (time + task_duration, free_index))
        return answer



