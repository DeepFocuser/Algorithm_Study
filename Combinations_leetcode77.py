from typing import List
'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.
'''
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:

#         array=[ i for i in range(1,n+1)]
#         result = []

#         def dfs(array = [], temp = []):
            
#             if len(temp)==k:
#                 result.append(temp[:])
#                 return

#             for i, a in enumerate(array):
#                 temp.append(a)
#                 dfs(array[i+1:], temp)
#                 temp.pop()

#         dfs(array, [])

#         return result

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def dfs(start, temp = []):
            
            if len(temp)==k:
                result.append(temp[:])
                return

            for i in range(start, n+1):
                temp.append(i)
                dfs(i+1, temp)
                temp.pop()

        dfs(1, [])

        return result
        
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
