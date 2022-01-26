# # 1. 재귀 방식 - 가장 느림
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#         return self.fib(n-1) + self.fib(n-2)

# # 2. tabulation 방식
# class Solution:
    
#     def fib(self, n: int) -> int:
        
#         dp = [""]*31
#         dp[0] = 0
#         dp[1] = 1

#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]

#         return dp[n]

# # 3. memoization 방식 - 책 참고 방식
# class Solution:

#     dp = [""]*31
#     def fib(self, n: int) -> int:

#         if n <= 1:
#             return n
        
#         if self.dp[n]: # 이게 미리 계산한거 리턴하는 것
#             return self.dp[n]

#         self.dp[n] = self.fib(n-1) + self.fib(n-2)

#         return self.dp[n]

# 4. 두 변수 방식 - 이런방식도 있구남. 
class Solution:

    def fib(self, n: int) -> int:
        
        x, y = 0, 1

        for _ in range(0, n):
            x, y = y, x+y

        return x

if __name__ == "__main__":

    sol=Solution()
    print(sol.fib(n = 2)) # 1
    print(sol.fib(n = 3)) # 2
    print(sol.fib(n = 4)) # 3
