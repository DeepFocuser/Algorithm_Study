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

# https://namu.wiki/w/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# 2. 플로이드 와샬 사용해보기
def solution(n, results):  
    
    # 이긴 놈은 1, 진놈은 -1 로 초기화 / 아무것도 아닌경우 0
    states = [[0]*n for _ in range(n)]
    for row, column in results:
        states[row-1][column-1] = 1 # 이긴애
        states[column-1][row-1] = -1 # 진애
    
    # 단순히 반복문을 3번 중첩시키기만 하면 되기 때문에 구현에 있어 크게 어려운 부분은 없다. 단, 유의하여야 할 점은 for문에서 가운데 노드(m)가 제일 위에 있어야 한다는 점이다. 어쨌든 매우 간결하다.
    for m in range(n):
        for s in range(n):
            for e in range(n):
                if s == e: # 대각선 제외
                    continue
                # s가 m을 이기고 m이 e를 이겼다면, s가 e를 이긴 것
                if states[s][m] == 1 and states[m][e] == 1:
                    states[s][e] = 1
                # s가 m에게 지고, m이 e에게 졌다면, s가 e에게 진 것
                if states[s][m] == -1 and states[m][e] == -1:
                    states[s][e] = -1
    answer = 0
    for state in states:
        if state.count(0) == 1:
            answer+=1
    return answer