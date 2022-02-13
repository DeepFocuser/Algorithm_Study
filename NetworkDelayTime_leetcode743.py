import heapq
from collections import defaultdict
from typing import List

'''
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times 
as directed edges times[i] = (ui, vi, wi), where ui is the source node,
vi is the target node, and wi is the time it takes for a signal to travel
from source to target.
We will send a signal from a given node k. 
Return the time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        distance = defaultdict(int)

        # 1. graph형태로 만들기(key, value)
        for u, v, cost in times:
            graph[u].append([v, cost]) # 시작지점, 끝지점, 비용

        # 2. 첫 비용, 시작지점을 담고있는 list 만들기
        Q = [(0, k)] # 비용, 시작지점

        # 3. heapq사용해서 최소 비용을 가진 주변경로를 뽑아준다. 
        while Q:
            cost, u = heapq.heappop(Q) # Q에서 가장 작은 비용을 가진 정점을 뽑는다.
            if u not in distance:
                distance[u] = cost
                for v, next_cost in graph[u]:
                    next_cost+=cost
                    heapq.heappush(Q, [next_cost, v])

        if len(distance) == n:
            return max(distance.values())

        return -1

if __name__ == "__main__":
    sol=Solution()
    print(sol.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)) # output 2
    print(sol.networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2)) # output 3
    print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 1)) # output 1
    print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)) # output -1
