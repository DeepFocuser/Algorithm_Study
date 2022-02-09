from typing import Optional
from listtoLinkedlist import ListNode, listtollist

# 1. 가장 쉬운 방법(value 리스트에 담기 -> 소팅 -> 새로운 listnode 만들기)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        deq = []
        if head:
            while head:
                deq.append(head.val)
                head=head.next

            deq = sorted(deq) # 오름차순 정렬
            next = None
            while deq:
                node = ListNode(val=deq.pop(), next=next)
                next = node

            return node
        return None

'''
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''
# 2. 생각중
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            pass
        return None

if __name__ == "__main__":
    print(Solution().sortList(head = listtollist([4,2,1,3]))) # [1,2,3,4]
    # print(Solution().sortList(head = listtollist([-1,5,3,4,0]))) # [-1,0,3,4,5]
    # print(Solution().sortList(head = listtollist([]))) # []