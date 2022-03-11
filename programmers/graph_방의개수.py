from collections import defaultdict

def solution(arrows):
    
    answer = 0 
    
    # cross상황 대비
    for_cross = 2
    
    # 정점 저장
    vertex = defaultdict(bool)
    
    # 간선 저장 x->y , y->x 저장
    edge = defaultdict(bool)
    
    # 오른쪽이 +, 왼쪽이 -
    # (x축, y축)
    move = [(0,1), (1,1), (1,0), (1,-1),
            (0,-1), (-1,-1), (-1,0), (-1,1)]
    # 첫번째 정점 True
    x_init, y_init = 0, 0
    vertex[(x_init, y_init)] = True
    for arrow in arrows:
        # 크로스 상황을 대비하기 위해 2칸씩 가기
        for _ in range(for_cross):
            x_position = x_init + move[arrow][0]
            y_position = y_init + move[arrow][1]
            if not vertex[(x_position, y_position)]: # 첫 방문
                vertex[(x_position, y_position)] = True
            elif vertex[(x_position, y_position)]: # 또 방문했는데,
                # 지나온 경로가 아닌 경우, 방 생성
                if not edge[(x_init, y_init, x_position, y_position)] or \
                not edge[(x_position, y_position, x_init, y_init)]:
                    answer+=1
            
            edge[(x_init, y_init, x_position, y_position)] = True
            edge[(x_position, y_position, x_init, y_init)] = True
            
            x_init, y_init = x_position, y_position 
    
    return answer