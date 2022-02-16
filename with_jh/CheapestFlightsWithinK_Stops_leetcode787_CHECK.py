# https://leetcode.com/problems/cheapest-flights-within-k-stops/

'''
There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates 
that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with "at most k stops." 
If there is no such route, return -1.
'''
from typing import List
from collections import defaultdict
import heapq

# k경유지 이내 - https://8iggy.tistory.com/115 참고
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        visit = {} # 이게 중요하다.

        # key, value 형태로 만들기
        for fro, to, price in flights:
            graph[fro].append([to, price])

        Q = [(0, src, -1)] # Price, from, stop 

        while Q:
            
            price, fro, stop  = heapq.heappop(Q)
            # 이미 최소경로인 경우 바로 return
            if fro == dst:
                return price

            ''' 
            아래 문제가 되는 예제 때문에, 인터넷 뒤져서 찾음
            heapq.heappop으로 price가 최소인 경로를 추출해왔기에 
            해당 노드를 방문하기 이전에 경유지가 더 적어야 한다.
            '''

            if fro not in visit or visit[fro] > stop: 
                visit[fro] = stop # 이미 지나온 경로에 현재 stop을 지정해줌
                if stop < k:
                    for t, p in graph[fro]:
                        heapq.heappush(Q, [p+price, t, stop+1])
        return -1

if __name__ == "__main__":
    # print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)) # 200
    # print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0)) # 500
    # print(Solution().findCheapestPrice(n = 3, flights = [[0,1,2],[1,2,1],[2,0,10]], src = 1, dst = 2, k = 1)) # 1
    # print(Solution().findCheapestPrice(n = 17, flights = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]], 
    # src = 13, dst = 4, k = 13)) 

    # 문제가 되는 예제
    print(Solution().findCheapestPrice(n = 13, flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],
    [0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],
    [10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],
    [3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],
    [5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],
    [9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],
    [12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],
    [0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],
    [2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],
    [12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],
    [5,6,34],[9,7,62],[5,3,67]], 
    src = 10, dst = 1, k = 10)) 

    # print(Solution().findCheapestPrice(n = 5, flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 
    # src = 0, dst = 2, k = 2)) 
    # print(Solution().findCheapestPrice(n = 18, flights = [[16,1,81],[15,13,47],[1,0,24],[5,10,21],[7,1,72],[0,4,88],[16,4,39],[9,3,25],[10,11,28],[13,8,93],[10,3,62],[14,0,38],[3,10,58],[3,12,46],[3,8,2],[10,16,27],[6,9,90],[14,8,6],[0,13,31],[6,4,65],[14,17,29],[13,17,64],[12,5,26],[12,1,9],[12,15,79],[16,11,79],[16,15,17],[4,0,21],[15,10,75],[3,17,23],[8,5,55],[9,4,19],[0,10,83],[3,7,17],[0,12,31],[11,5,34],[17,14,98],[11,14,85],[16,7,48],[12,6,86],[5,17,72],[4,12,5],[12,10,23],[3,2,31],[12,7,5],[6,13,30],[6,7,88],[2,17,88],[6,8,98],[0,7,69],[10,15,13],[16,14,24],[1,17,24],[13,9,82],[13,6,67],[15,11,72],[12,0,83],[1,4,37],[12,9,36],[9,17,81],[9,15,62],[8,15,71],[10,12,25],[7,6,23],[16,5,76],[7,17,4],[3,11,82],[2,11,71],[8,4,11],[14,10,51],[8,10,51],[4,1,57],[6,16,68],[3,9,100],[1,14,26],[10,7,14],[8,17,24],[1,11,10],[2,9,85],[9,6,49],[11,4,95]], 
    # src = 7, dst = 2, k = 6)) 