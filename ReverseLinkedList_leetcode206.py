from typing import Optional
from unittest import result
from listtoLinkedlist import ListNode, listtollist

# # 1. head 자체를 이용해보자
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         temp = None # 처음에는 None으로 지정
#         while head: # head가 None이 아닐때까지 while문 돌리기
#             temp = ListNode(val = head.val, next = temp)
#             head = head.next
        
#         return temp

# 2. 새로운 ListNode 공간을 할당하지 않는 방법을 생각해보자
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        while head:
            next = head.next # head.next를 next 변수에 저정

            # 아래에서 head.next가 prev에 할당되면 위의 next 가 바뀐다고 생각했으나,
            # 그런게 아니었음. 따라서 아래처럼 해도 됨.
            head.next = prev  
            prev = head

            head = next # head에 next 할당

        return prev

# 3. 재귀로 가능? 가능하다고 한다. 책에 있는 코드
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head: Optional[ListNode], prev: ListNode = None) -> Optional[ListNode]:
            if not head:
                return prev
            next = head.next 
            head.next = prev
            return reverse(next, head)

        return reverse(head)

if __name__ == "__main__":
    print(Solution().reverseList(head = listtollist([1,2,3,4,5]))) # [5,4,3,2,1]
    print(Solution().reverseList(head = listtollist([1,2]))) # [2,1]
    print(Solution().reverseList(head = listtollist([]))) # []