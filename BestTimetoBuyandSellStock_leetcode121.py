from typing import List

# # 시간초과
# class Solution:

#     def maxProfit(self, prices: List[int]) -> int:

#         temp = 0
#         for i in range(len(prices)-1):

#             max_value = max(prices[i+1:])-prices[i]
#             if max_value > temp:
#                 temp = max_value                                  

#         return temp 

# 됬다.. 
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        profit = {"buy": prices[0], "sell" : prices[0]}
        length = 0

        for i in range(1, len(prices)):

            # 최소점, 최대점이 다음 점보다 작은 경우, 최대점에 다음점 저장 및 최대 길이 갱신
            if profit["buy"] <= profit['sell'] < prices[i]:
                if length < prices[i]-profit["buy"]:
                    profit["sell"] = prices[i]
                    length = profit["sell"]-profit["buy"]

            # 최소점이 다음점보다 큰 경우 최소점, 최대점 이동
            elif profit["buy"] > prices[i]: # >= , > 상관없음
                profit["buy"] = prices[i]
                profit["sell"] = prices[i]

        return length

import sys
# 책 풀이법
class Solution:

    #  [7,1,5,3,6,4]
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 10**4
        for price in prices:
            buy = min(prices, buy)
            profit = max(, price-buy)

if __name__ == "__main__":
    '''
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    '''
    print(Solution().maxProfit(prices = [7,1,5,3,6,4])) # output 5

    # Explanation: In this case, no transactions are done and the max profit = 0.
    print(Solution().maxProfit(prices = [7,6,4,3,1])) # output 0
    print(Solution().maxProfit(prices = [3,2,6,5,0,3])) # output 4
    print(Solution().maxProfit(prices = [4,1,2])) # output 1
    print(Solution().maxProfit(prices = [1,2])) # output 0
