from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

path_bfs = []
# Breadth First Search using queue - 재귀 불가
def bfs(graph, start_node, end_node):

    start_node = start_node.upper()
    end_node = end_node.upper()

    visit = {}
    queue = deque()

    queue.append(start_node)

    while queue:
        node = queue.popleft() # 첫번째 요소부터 pop
        if node not in visit:
            visit[node] = True

            if node == end_node:
                # visit.keys()는 mutable 이므로 복사를 해준다
                path_bfs.append(list(visit.keys()))

            # 왼쪽부터 오른쪽으로 검사
            queue.extend(graph[node])

    return list(visit.keys())

path_dfs = []
# depth first search using stack
def dfs(graph, start_node, end_node):

    start_node = start_node.upper()
    end_node = end_node.upper()

    visit = {}
    queue = deque()

    queue.append(start_node)

    while queue:
        node = queue.pop() # 마지막 요소부터 pop
        if node not in visit:
            visit[node] = True

            if node == end_node:
                # visit.keys()는 mutable 이므로 복사를 해준다
                path_dfs.append(list(visit.keys()))

            # why reverse ? 왼쪽에서 오른쪽으로 검사
            queue.extend(reversed(graph[node]))
            #queue.extend(graph[node])

    return list(visit.keys())

# dfs recursive!
path_dfs_recur = []
def dfs_recursive(graph, start_node, end_node, visit=dict()):

    start_node = start_node.upper()
    end_node = end_node.upper()
    visit[start_node] = True

    if start_node == end_node:
        # visit.keys()는 mutable 이므로 복사를 해준다
        path_dfs_recur.append(list(visit.keys()))

    for node in graph[start_node]:
        if node not in visit:
            dfs_recursive(graph, node, end_node, visit)

    return list(visit.keys())

if __name__ == "__main__":

    print("bfs :",bfs(graph, start_node='A', end_node="C"))
    print("bfs path :", path_bfs)
    # print("dfs :",dfs(graph, start_node='A', end_node="D"))
    # print("dfs path :", path_bfs)
    # print("dfs_recursive :",dfs_recursive(graph, start_node='A', end_node="D"))
    # print("dfs_recursive path :", path_bfs)
    '''
    print
    bfs : ['A', 'B', 'C', 'H', 'D', 'I', 'J', 'M', 'E', 'G', 'K', 'F', 'L']
    bfs path : [['A', 'B', 'C', 'H', 'D']]
    dfs : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    dfs path : [['A', 'B', 'C', 'H', 'D']]
    dfs_recursive : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    dfs_recursive path : [['A', 'B', 'C', 'H', 'D']]
    '''