from typing import Optional
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
        
        result = None
        while head:
            temp = head.next # head.next를 temp변수에 저정

            # 아래에서 head.next가 result값이 할당되면 위의 temp가 바뀐다고 생각했으나,
            # 그런게 아니었음. 따라서 아래처럼 해도됨.
            head.next = result  
            result = head

            head = temp # head에 temp 할당

        return result

if __name__ == "__main__":
    print(Solution().reverseList(head = listtollist([1,2,3,4,5]))) # [5,4,3,2,1]
    # print(Solution().reverseList(head = listtollist([1,2]))) # [2,1]
    # print(Solution().reverseList(head = listtollist([]))) # []