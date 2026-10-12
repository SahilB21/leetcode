class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        ongoing = []
        available = [i for i in range(n)]
        heapify(ongoing)
        heapify(available)
        count = [0 for i in range(n)]
        for start, end in sorted(meetings):
            while ongoing and ongoing[0][0] <= start:
                room = heapq.heappop(ongoing)[1]
                heapq.heappush(available, room)
            if len(available) > 0:
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(ongoing, [end, room])
            else:
                curr = heapq.heappop(ongoing)
                room = curr[1]
                currEnd = curr[0]
                heapq.heappush(available, room)
                count[room] += 1
                newRoom = heapq.heappop(available)
                newEnd = currEnd + end - start
                heapq.heappush(ongoing, [newEnd, newRoom])
        return count.index(max(count))