from collections import defaultdict
# 주어진 항공권을 모두다 사용해야하는 것이 킬포인트 - 다시 봐야하는 문제
def solution(tickets):
    
    answer = []
    graph = defaultdict(list)
    for start, destination in tickets:
        graph[start].append(destination)
    
    # 내림차순으로 만들기 - pop할때 순서가 앞서는 경로를 내뱉기 위함
    for value in graph.values():
        value.sort(reverse=True)
    
    '''
    입력값 〉	[["ICN", "1"], ["1", "DEST"], ["ICN", "2"], ["2", "3"], ["3", "ICN"]]
    기댓값 〉	["ICN", "2", "3", "ICN", "1", "DEST"]
    '''
    # graph[begin] 가 False인경우 -> 마지막이라는 말임.
    stack = ["ICN"]
    while stack:
        begin = stack[-1]
        if graph[begin]:
            stack.append(graph[begin].pop())  
        else:
            answer.append(stack.pop())
    return answer[::-1]