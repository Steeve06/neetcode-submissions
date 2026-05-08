class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src,dst,time in times:
            adj[src].append((dst,time))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            t1, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            t = t1

            for node1,t2 in adj[node]:
                if node1 not in visit:
                    heapq.heappush(minHeap,((t2+t1),node1))

        return t if len(visit) == n else -1