from collections import defaultdict, deque

# tree 문제로 바라보면 편하다
def solution(begin, target, words):
    
    depth = 0
    # 1. target이 words에 없는 경우
    if not target in words:
        return depth # 0
    
    # 2. 방문 목록 만들기
    visited=defaultdict(bool)
    for word in words:
        visited[word] = False
    
    # 한 글자만 다른 경우에만 True 반환
    def compare(a_string, b_string):
        count = 0
        for a,b in zip(a_string, b_string):
            if a != b:
                count+=1
        if count == 1:
            return True
        return False
    
    # 3. 계산하기 
    stack = deque([[begin, depth]]) # 뒤에 순서 변수 하나를 더 두는 것이 핵심
    while stack:
        begin, depth = stack.pop() # or pop()
        if begin == target: # begin == target인 경우 break
            return depth

        for candidate in words:
            # 1글자씩만 변환이 가능하므로!
            if compare(begin, candidate) and not visited[candidate]:
                visited[candidate] = True
                stack.append([candidate, depth+1]) 
 
    return 0