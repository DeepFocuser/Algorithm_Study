# 방법1
answer = 0
def solution(numbers, target):

    length = len(numbers)
    numbers = [0] + numbers # tree만들어서 dfs로
    
    def dfs(value=0, index=0):

        global answer
        
        if index == length:
            if value == target:
                answer+=1
                return
            else:
                return # 탈출 조건

        dfs(value+numbers[index+1], index+1)
        dfs(value-numbers[index+1], index+1)
    
    dfs()
    
    return answer

# 방법2
answer = 0
def dfs(graph=None, index=0, value=0, target=None):

    global answer 
    length = len(graph) - 1

    if index == length:
        if value == target:
            answer+=1
            return 
        else:
            return 

    dfs(graph, index+1, value+graph[index+1], target)
    dfs(graph, index+1, value-graph[index+1], target)

def solution(numbers, target):

    numbers = [0] + numbers # tree만들어서 dfs로
    dfs(graph=numbers, target=target)
    return answer 


print(solution([4, 1, 2, 1], 4))