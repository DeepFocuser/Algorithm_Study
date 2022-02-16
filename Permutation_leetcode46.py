from collections import defaultdict
class Solution:
    def permute(self, nums):
        
        checked = defaultdict(bool)
        result = []
        def dfs(level=0, temp=[]): 
            if level == len(nums): 
                result.append(temp[:]) # temp가 아래의 for문에서 게속 바뀌기 때문에 복사를 해줘야함
                return
            for i, n in enumerate(nums):
                if checked[i]:
                    continue
                checked[i] = True
                temp.append(n)
                dfs(level+1)
                temp.pop()
                checked[i]=False
        dfs()
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute(nums = [1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(sol.permute(nums = [0,1])) # [[0,1],[1,0]]
    print(sol.permute(nums = [1])) # [[1]]
