# from itertools import combinations 
# 시간 초과
# def solution(distance, rocks, n):
#     rocks.sort()
#     cb=list(combinations(rocks, n))
#     path=[0]+rocks+[distance]    
#     max_value = 0
#     while cb:
#         temp = path.copy()
#         nrock = cb.pop()
#         for rock in nrock:
#             temp.remove(rock)        
#         min_value = 1000000000
#         for i in range(len(temp)-1):
#             rock_distance=temp[i+1]-temp[i]
#             if min_value > rock_distance:
#                 min_value = rock_distance
#         if max_value < min_value:
#             max_value = min_value
#     return max_value

# 최대값 구하는 케이스
# 이분탐색 범위를 정하고, 탐색대상, 범위를 결정짓는 기준을 정하자.
def solution(distance, rocks, n):
    
    # 1. 정렬
    rocks.sort()
    rocks = rocks + [distance]
    rocks_length = len(rocks)
    left, right = 1, distance # 이분탐색의 범위는 바위사이의 최소간격, 최대간격
    answer = 0
    
    # 2. 이분 탐색
    while left <= right:
        mid = (left + right) // 2 # 일단 정답이라 생각하기
        n_counter = 0
        start_position = 0
        current = 0
        for i in range(rocks_length):
            '''
            1. current에 돌간의 간격을 순차적으로 더해간다.
            2. current에 어떤 돌간의 간격이 더해졌는데, 그 값이  mid를 넘어버린다면
            그 돌은 n_counter 할 대상에서 제외하고, current를 0으로 초기화 한다.
            예를 들어, 바로 이전까지의 합쳐진 돌 간격들이 mid보다 짧아서 제거되엇고, 
            다음 번의 돌 간격이 더해졌는데, 제거해야할 대상에 포함이 안되었다면, 
            이 경우 돌 간격이 mid보다 긴 것이다. 따라서 제거되야할 대상이 아니므로
            건너뛴다.
            '''
            current += (rocks[i]-start_position) 
            if current < mid: # mid보다 작은 값들
                n_counter+=1
            else:
                current = 0     
                
            start_position = rocks[i]
        
        # 이 아래부분이 정말 헷갈린다.
        if n_counter<=n: # mid값을 늘리자
            left = mid+1
        else: # n_counter>n: # mid값을 줄이자
            right = mid-1 # 왜 꼭 여기에 와야할까?
            answer = right
            
    return answer