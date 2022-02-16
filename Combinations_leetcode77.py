from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        pass

if __name__ == "__main__":
    sol = Solution()

    '''
    [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
    ]
    '''
    print(sol.combine(n = 4, k = 2))
    '''
    Output: [[1]]
    '''
    print(sol.combine(n = 1, k = 1)) 
