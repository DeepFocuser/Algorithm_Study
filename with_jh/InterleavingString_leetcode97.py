# Follow up: Could you solve it using only O(s2.length) additional memory space?
# dfs 든 bfs든 상관없다.
from collections import deque
# 이 방법은 외우자
class Solution(object):
    def isInterleave(self, s1, s2, s3):

        if len(s1+s2) == len(s3):
            temp = deque([[0, 0]])
            visited = set() # 방문한 곳을 또 방문하지 않기위해
            while temp:
                x, y = temp.popleft()
                if x == len(s1) and y == len(s2):
                    return True
                if x < len(s1) and s1[x] == s3[x+y] and (x+1, y) not in visited: 
                    temp.append([x+1, y])
                    visited.add((x+1, y))
                if y < len(s2) and s2[y] == s3[x+y] and (x, y+1) not in visited:
                    temp.append([x, y+1])
                    visited.add((x, y+1))
            return False

        return False

if __name__ == "__main__":

    print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")) # true
    print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")) # false
    print(Solution().isInterleave(s1 = "", s2 = "", s3 = "")) # true

