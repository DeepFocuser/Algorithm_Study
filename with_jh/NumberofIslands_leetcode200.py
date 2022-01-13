from typing import List
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.
'''
from collections import deque

# dfs, bfs를 사용하즈아

class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        
        row_length = len(grid)
        column_length = len(grid[0])
        number_of_island = 0

        def find_island_recursive(i,j):

            grid[i][j] = "0"

            # 4방향 체크하기
            if j > 0 and grid[i][j-1] == "1": # 왼쪽
                find_island_recursive(i,j-1)
            if j < len(grid[0])-1 and grid[i][j+1] == "1": # 오른쪽
                find_island_recursive(i,j+1)
            if i < len(grid)-1 and grid[i+1][j] == "1": # 상
                find_island_recursive(i+1,j)
            if i > 0  and grid[i-1][j] == "1": # 하
                find_island_recursive(i-1,j)
        
        def find_island(positions, grid):

            deq = deque()
            deq.append(positions)

            # 상하좌우 판단해서 1이 한개 있으면 0으로 바꾸기
            while deq: 
                i, j = deq.pop()
                grid[i][j] = "0" 

                # 4방향 체크하기
                if j > 0 and grid[i][j-1] == "1": # 왼쪽
                    deq.append([i,j-1])
                    grid[i][j-1] = "0"
                if j < len(grid[0])-1 and grid[i][j+1] == "1": # 오른쪽
                    deq.append([i,j+1])
                    grid[i][j+1] = "0"
                if i < len(grid)-1 and grid[i+1][j] == "1": # 상
                    deq.append([i+1,j])
                    grid[i+1][j] = "0"
                if i > 0  and grid[i-1][j] == "1": # 하
                    deq.append([i-1,j])
                    grid[i-1][j] = "0"

        for i in range(row_length):
            for j in range(column_length):
                if grid[i][j] == "1":
                    # grid 자체를 바꿔야 함
                    #find_island([i,j], grid)
                    find_island_recursive(i,j)
                    number_of_island+=1

        return number_of_island

if __name__ == "__main__":
    sol = Solution()
    '''
    Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
    '''
    print(sol.numIslands(grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))
    print(sol.numIslands(grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]))

