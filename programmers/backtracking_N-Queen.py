from collections import defaultdict

answer = 0
def solution(n):

    visited = defaultdict(int)

    def valid(row):
        for r in range(row):
            if visited[r] == visited[row] or \
            abs(visited[r]-visited[row]) == row-r: # 같은 열에 존재 or 대각선
                return False

        return True

    def n_queen(row):

        global answer
        if row == n:
            answer+=1
            return
        else:
            for column in range(n):
                visited[row] = column
                if valid(row):
                    n_queen(row+1)
    n_queen(0)
    return answer
