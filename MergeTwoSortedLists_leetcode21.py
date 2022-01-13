# daleseo.com/python-typing/

from typing import Optional
from listtoLinkedlist import ListNode, listtollist
# Definition for singly-linked list.

# 1. 통과는 됬으나, 뭔가 찜짐하다. 효율적인 방법을 생각해보자
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = []
        # list1 값 뽑아내기
        while list1 != None:
            l1.append(list1.val)
            list1=list1.next       

        l2 = []
        # list2 값 뽑아내기
        while list2 != None:
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

# 2. 생각중
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    print(Solution().mergeTwoLists(list1 = listtollist([1,2,4]), list2 = listtollist([1,3,4]))) # [1,1,2,3,4,4]
    print(Solution().mergeTwoLists(list1 = listtollist([]), list2 = listtollist([])))  # []
    print(Solution().mergeTwoLists(list1 = listtollist([]), list2 = listtollist([0]))) # [0]