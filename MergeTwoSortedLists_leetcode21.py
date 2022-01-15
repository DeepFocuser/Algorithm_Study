# daleseo.com/python-typing/

from typing import List, Optional
from listtoLinkedlist import ListNode, listtollist
# Definition for singly-linked list.

# 1. 통과는 됬으나, 뭔가 찜짐하다. 효율적인 방법을 생각해보자
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = []
        # list1 값 뽑아내기
        while list1:
            l1.append(list1.val)
            list1=list1.next       

        l2 = []
        # list2 값 뽑아내기
        while list2:
            l2.append(list2.val)
            list2=list2.next

        l = l1+l2
        l.sort()
        
        if l:
            temp = []
            
            for arr in l:
                temp.append(ListNode(val=arr))
            
            for i in range(len(temp)-1, 0, -1):
                temp[i-1].next = temp[i]

            return temp[0]
        else:
            return None

# 2. 새로운 공간인 ListNode 생성 / list1, list2 실시간 비교
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # list1, list2는 오름차순!!!

        space=ListNode(val=None)
        repeat = space # 아래에서 repeat가 바뀌더라도 space안의 모든것은 유지된다.

        # repeat는 space의 next에 실시간으로 채워넣는 역할
        # 1. 둘중 하나가 빨리 끝나겠지?
        while list1 and list2:
            
            if list1.val > list2.val: 
                repeat.next=list2
                list2 = list2.next
            else:
                repeat.next=list1
                list1 = list1.next

            repeat = repeat.next

        # list1이 남았다면 repeat.next에 추가
        # list2가 남았다면 repeat.next에 추가 
        if list1:
            repeat.next = list1     
        else:
            repeat.next = list2
            
        return space.next


# 3. 재귀구조로 풀어보기 - 쉽지 않다. / 다른 사람 풀이를 본 후 / 손으로 그려봄.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or (list2 and list1.val > list2.val): # list1이 반드시 앞에 와야함 - or : 앞에가 참이면 뒤에도 참
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1
        

if __name__ == "__main__":
    print(Solution().mergeTwoLists(list1 = listtollist([1,2,4]), list2 = listtollist([1,3,4]))) # [1,1,2,3,4,4]
    #print(Solution().mergeTwoLists(list1 = listtollist([]), list2 = listtollist([])))  # []
    #print(Solution().mergeTwoLists(list1 = listtollist([]), list2 = listtollist([0]))) # [0]