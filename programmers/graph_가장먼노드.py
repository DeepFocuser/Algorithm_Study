from collections import defaultdict
import heapq

def solution(n, edge):
    
    graph = defaultdict(list)
    distance = defaultdict(int)

    for k, v in edge:
        # 양방향 / 거리 1로 통일
        graph[k].append([v, 1]) 
        graph[v].append([k, 1])
    
    Q = [(0, 1)] # 간선 비용, 시작 노드 / 시작 노드는 비용이 0
    while Q:
        cost, start_node = heapq.heappop(Q) 
        if start_node not in distance:
            distance[start_node] = cost
            for next_node, next_cost in graph[start_node]:
                heapq.heappush(Q, [next_cost+cost, next_node])
                
    answer = 0
    max_value=max(distance.values())
    for value in distance.values():
        if max_value == value:
            answer+=1

    return answer