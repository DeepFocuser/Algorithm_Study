# 1. 간선 개수 구하기 방식 using dfs - 내 방식
def solution(n, computers):
    
    # 1. 방문할 컴퓨터 담아 놓기
    stack = []
    for i in range(n):
        stack.append(i)

    # 2. 방문 여부
    visited = [False]*n
     
    # 3. 구해볼까나
    line_number = 0
    while stack:
        temp = stack.pop() 
        for i, connected in enumerate(computers[temp]):
            if i == temp and not visited[i]: # 나 자신일 경우는 방문여부만 체크하기
                visited[i] = True
                continue
                
            if connected == 1 and not visited[i]:
                stack.append(i)
                visited[i] = True
                line_number+=1
    
    # n이 3이고, 간선 개수(line_number)가 2이면 네트워크 개수는 n-line_number 이다
    return n-line_number

# 2. 네트워크 방문으로 구하기 - dfs, dfs
from collections import deque
def solution(n, computers):
    
    visited = [False]*n
    answer = 0
    
    def bfs(i, computers, visited):
        deq = deque([i])
        while deq:
            temp=deq.popleft()
            for j, computer in enumerate(computers[temp]):
                if temp == j:
                    continue
                if computer == 1 and not visited[j]:
                    visited[j] = True
                    deq.append(j)

    def dfs(i, computers, visited):
        deq = deque([i])
        while deq:
            temp=deq.pop()
            for j, computer in enumerate(computers[temp]):
                if temp == j:
                    continue
                if computer == 1 and not visited[j]:
                    visited[j] = True
                    deq.append(j)

    def dfs_recursive(i, computers, visited):
        for j, computer in enumerate(computers[i]):
            if i == j:
                continue
            if computer == 1 and not visited[j]:
                visited[j] = True
                dfs(j, computers, visited)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            # bfs(i, computers, visited)
            dfs(i, computers, visited)
            # dfs_recursive(i, computers, visited)
            answer+=1
            
    return answer