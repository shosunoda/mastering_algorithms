import heapq

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        # Priority queue: stores (-distance, left, right)
        #   left, right represent empty interval (left, right)
        #   -distance ensures the largest interval is popped first
        # Initially, the whole room is empty (-n means max gap)
        self.heap = [(-n, -1, n)]

        # Neighbor map: each seat stores [left_neighbor, right_neighbor]
        # Dummy head (-1) and tail (n) make edge cases simple
        self.neighbors = {
            -1: [None, n],
            n: [-1, None],
        }

    def seat(self) -> int:
        # Remove invalid intervals until the top of heap matches current state
        while True:
            _, left, right = self.heap[0]
            left_valid = self.neighbors.get(left, [None, None])[1] == right
            right_valid = self.neighbors.get(right, [None, None])[0] == left
            if left_valid and right_valid:
                break
            heapq.heappop(self.heap)  # discard stale interval

        _, left, right = heapq.heappop(self.heap)

        if left == -1:
            seat = 0  # no one on the left
        elif right == self.n:
            seat = self.n - 1  # no one on the right
        else:
            seat = (left + right) // 2  # sit in the middle

        # Push new intervals back into heap (left and right halves)
        if left == -1:
            # Edge case: start of room (0 .. right)
            new_distance = right - 1
            heapq.heappush(self.heap, (-new_distance, seat, right))
        elif right == self.n:
            # Edge case: end of room (left .. n-1)
            new_distance = self.n - 2 - left
            heapq.heappush(self.heap, (-new_distance, left, seat))
        else:
            # General case: two new intervals created
            left_distance = (seat - left) // 2
            right_distance = (right - seat) // 2
            heapq.heappush(self.heap, (-left_distance, left, seat))
            heapq.heappush(self.heap, (-right_distance, seat, right))

        # Update neighbor map to include this new seat
        self.neighbors[seat] = [left, right]
        self.neighbors[left][1] = seat
        self.neighbors[right][0] = seat

        return seat

    def leave(self, seat: int) -> None:
        left, right = self.neighbors[seat]

        # Merge the two intervals around the leaving seat
        if left == -1:
            distance = right  # gap from 0 to right
            heapq.heappush(self.heap, (-distance, -1, right))
        elif right == self.n:
            distance = self.n - 1 - left
            heapq.heappush(self.heap, (-distance, left, self.n))
        else:
            distance = (right - left) // 2
            heapq.heappush(self.heap, (-distance, left, right))

        # Update neighbor map to remove the leaving seat
        self.neighbors[left][1] = right
        self.neighbors[right][0] = left
        del self.neighbors[seat]
