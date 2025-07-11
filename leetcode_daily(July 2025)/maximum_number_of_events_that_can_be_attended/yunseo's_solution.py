import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        cnt = 0
        min_heap = []
        day = 0
        i = 0

        # sort events by their start day
        events.sort()

        while i < n or min_heap:
            # if there are no events today, skip to next day
            if not min_heap:
                day = events[i][0]
            
            # add all events that can be attended today
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1]) 
                i += 1
            
            # attend the event that ends the earliest
            heapq.heappop(min_heap)
            cnt += 1
            day += 1

            # remove all events that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
        return cnt