def solution(brown, yellow):
   
    area=brown+yellow # 넓이 
    for y in range(3, area+1): # 3 이상부터만 사이에 yellow 오는것 가능
        if area % y == 0:
            x = area // y
            if x >= y and (x-2) * (y-2) == yellow:
                return [x, y]