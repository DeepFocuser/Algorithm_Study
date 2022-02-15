from typing import List, Optional
from listtoLinkedlist import listtollist, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a1=[]
        a2=[]
        while l1 or l2:
            if l1:
                a1.append(l1.val)
                l1=l1.next
            if l2:
                a2.append(l2.val)
                l2=l2.next

        as1=0
        for i,a in enumerate(a1):
            as1+=(a*(10**i))

        as2=0   
        for i, a in enumerate(a2):
            as2+=(a*(10**i))

        print(as1, as2)
        a2 = 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.addTwoNumbers(l1 = listtollist([2,4,3]), l2 = listtollist([5,6,4])))
    # print(sol.addTwoNumbers(l1 = listtollist([0]), l2 = listtollist([0])))
    # print(sol.addTwoNumbers(l1 = listtollist([9,9,9,9,9,9,9]), l2 = listtollist([9,9,9,9])))