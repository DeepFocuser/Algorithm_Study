from typing import Optional
from listtoLinkedlist import ListNode, listtollist

# 1. 가장 쉬운 방법(value 리스트에 담기 -> 소팅 -> 새로운 listnode 만들기)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        deq = []
        if head:
            temp = head # temp는 head를 참조함
            while temp:
                deq.append(temp.val)
                temp=temp.next 
            deq.sort()

            temp = head # temp는 head를 참조함
            for i in range(len(deq)):
                temp.val=deq[i]
                temp = temp.next

            return head
        return None

'''
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''
# # 2. 생각중
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         if head:
#             pass
#         return None

if __name__ == "__main__":
    print(Solution().sortList(head = listtollist([4,2,1,3]))) # [1,2,3,4]
    # print(Solution().sortList(head = listtollist([-1,5,3,4,0]))) # [-1,0,3,4,5]
    # print(Solution().sortList(head = listtollist([]))) # []