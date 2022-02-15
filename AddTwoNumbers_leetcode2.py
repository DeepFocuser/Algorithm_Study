import functools
from typing import Optional
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

        # as1=0
        # for i,a in enumerate(a1):
        #     as1+=a*(10**i)

        # as2=0   
        # for i, a in enumerate(a2):
        #     as2+=a*(10**i)
        tonumber=lambda x,y : 10*x+y
        as1= functools.reduce(tonumber,a1[::-1])    
        as2= functools.reduce(tonumber,a2[::-1])
        temp = str(as1+as2)

        # LinkedList 만들기
        prev = None
        for t in temp: # 807
            node = ListNode(t)
            node.next = prev
            prev = node
        return node


# 전가산기 - 책 참고
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry: # carry도 조건문에 있다.
            sum = 0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next

            carry, val = divmod(sum + carry, 10)

            head.next = ListNode(val)
            head = head.next
        
        return root.next

if __name__ == "__main__":
    sol = Solution()
    print(sol.addTwoNumbers(l1 = listtollist([2,4,3]), l2 = listtollist([5,6,4])))
    print(sol.addTwoNumbers(l1 = listtollist([0]), l2 = listtollist([0])))
    print(sol.addTwoNumbers(l1 = listtollist([9,9,9,9,9,9,9]), l2 = listtollist([9,9,9,9])))
    print(sol.addTwoNumbers(l1 = listtollist([2,4,9]), l2 = listtollist([5,6,4,9])))
