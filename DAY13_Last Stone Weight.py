class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inverted = [-i for i in stones]
        heapq.heapify(inverted)

        while len(inverted) > 1:
            first = heapq.heappop(inverted)
            second = heapq.heappop(inverted)

            if second != first:
                heapq.heappush(inverted, -(abs(first)-abs(second)))


        return -inverted[0] if inverted else 0
