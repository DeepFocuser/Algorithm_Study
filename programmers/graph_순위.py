# 1. 집합자료형 사용
from collections import defaultdict
def solution(n, results):
    
    graph_win = defaultdict(set)
    graph_lose = defaultdict(set)

    for win, lose in results:
        graph_win[win].add(lose)
        graph_lose[lose].add(win)
    
    for i in range(1, n+1):
        # win은 lose가 이긴 것들에도 이김
        lose_set = graph_win[i].copy()
        # 5, [[1, 2], [4, 5], [3, 4], [2, 3]]  와 같은 경우 대비
        while lose_set:
            lose = lose_set.pop()
            graph_win[i].update(graph_win[lose])
            lose_set.update(graph_win[lose])
            
        # lose는 win을 이긴 것들에도 짐
        win_set = graph_lose[i].copy()
        # 5, [[1, 2], [4, 5], [3, 4], [2, 3]]  와 같은 경우 대비
        while win_set:
            win = win_set.pop()
            graph_lose[i].update(graph_lose[win])
            win_set.update(graph_lose[win])
    
    answer = 0
    for i in range(1, n+1):
        if len(graph_win[i] | graph_lose[i]) == n-1:
            answer+=1
    
    return answer

# 2. 플로이드 와샬 사용해보기