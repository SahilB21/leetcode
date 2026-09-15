import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num] += 1
        heap = []
        for pair in dictionary:
            heapq.heappush(heap, (dictionary[pair], pair))
            if (len(heap)) > k:
                heapq.heappop(heap)
        final = []
        for item in heap:
            final.append(item[1])
        return final
        
        