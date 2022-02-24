# 최소값 구하는 케이스
def solution(n, times):

    times.sort()
    answer=0
    # 1. 범위 정하기 (최저 시간, 최대 시간)
    left, right = min(times), max(times)*n
    while left <= right:
        # 2. 중간값 구하기
        middle = (left+right) // 2
        number = 0
        # 3. 각 시간들로 나눠서 인원수 구하기
        for time in times:
            number += middle//time
        
        # 이 아래부분이 정말 헷갈린다.
        # 4. n보다 작은 경우 - 시간을 늘려야함
        if number < n:
            left = middle + 1
        else: # number >= n - 시간을 줄이자
            answer = middle
            right = middle - 1
        
    return answer