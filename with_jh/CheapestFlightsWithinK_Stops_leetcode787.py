from email.policy import default
from typing import List
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

'''
There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates 
that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.
'''
from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        dist = defaultdict(int)

        # key, value 형태로 만들기
        for fro, to, price in flights:
            graph[fro].append([to, price])

        print(graph)
        # queue = deque()
        # queue.append([src,0])

        # while queue:
        #     node = queue.popleft() # 첫번째 요소부터 pop
        #     if node[0] == dst:
            
        #     queue.append()
        # return list(visit.keys())


if __name__ == "__main__":
    '''
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
    Output: 200
    Explanation: The graph is shown.
    The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
    '''
    print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)) # 200

    '''
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
    Output: 500
    Explanation: The graph is shown.
    The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
    '''
    #print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0)) # 500