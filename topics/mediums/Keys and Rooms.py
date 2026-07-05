from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #  there are n rooms labelled from 0 to n-1
        # all rooms are locked byt room 0 
        # our goal is to visit all rooms 
        #  we need a key to visit each room 
        # when we visit a room, we find keys, that correspodn to specific room 
        # 
        next_rooms = deque()
        next_rooms.append(0)
        visited = set()
        while next_rooms:
            cur_room = next_rooms.pop()
            visited.add(cur_room)
            for next_key in rooms[cur_room]:
                if next_key in visited:
                    continue
                next_rooms.append(next_key)

        return len(visited) == len(rooms)