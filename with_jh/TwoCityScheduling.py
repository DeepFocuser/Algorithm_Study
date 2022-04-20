
from typing import List

class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)//2
        aCost = []
        bCost = []
        
        costs.sort(key=lambda x : abs(x[0]-x[1]), reverse=True) # 내림차순
        
        '''
        1. a-b로 costs를 내림차순 정렬 - 이걸 생각하는게 핵심인듯.
        2. costs를 앞에서부터 순회하며 작은 것을 aCost, bCost 리스트에 포함하기(aCost, bCost 가 길이가 n이 될때까지)
        3. aCost, bCost 둘중 하나만 길이가 n이 된 경우 처리하기 -> 만약 len(aCost)==n 인 경우,  bCost에 b 담아주기 / 반대도 마찬가지   
        '''
        for a, b in costs:
            
            if len(aCost) == n:
                bCost.append(b)
                continue
                
            if len(bCost) == n:
                aCost.append(a)
                continue
                
            if a<=b:
                if len(aCost) < n:
                    aCost.append(a)
            else:
                if len(bCost) < n:
                    bCost.append(b)
        
        return sum(aCost+bCost)


if __name__ == "__main__":

    print(Solution().twoCitySchedCost(costs = [[10,20],[30,200],[400,50],[30,20]])) # 110
    print(Solution().twoCitySchedCost(costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])) # 1859 
    print(Solution().twoCitySchedCost(costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]])) # 3086 
