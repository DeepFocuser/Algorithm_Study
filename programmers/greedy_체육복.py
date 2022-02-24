def solution(n, lost, reserve):
    
    # 체육복을 가져온 학생이 체육복을 도난당했을 경우 처리하기
    # lost, reserve에 둘다 있는 경우 처리
    lost = set(lost)
    reverse = set(reserve)
    intersection = lost.intersection(reserve)
    
    # 공통된 부분 빼고 list로 변환하기
    lost = list(lost.difference(intersection))
    reverse = list(reverse.difference(intersection))
    
    # 정렬하기
    lost.sort()
    reverse.sort()
    reverse_length = len(reverse)

    # n에서 lost숫자 빼놓기
    answer = n - len(lost) 
    
    start_index = 0
    for l in lost:
        for i in range(start_index, reverse_length):
            # reverse[i] 기준으로 왼쪽, 오른쪽만 커버 가능하므로
            if reverse[i]-1 == l or reverse[i]+1 == l:
                answer+=1
                start_index+=1
                break
    return answer