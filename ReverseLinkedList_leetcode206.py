from typing import Optional
from listtoLinkedlist import ListNode, listtollist

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    print(Solution().reverseList(head = listtollist([1,2,3,4,5]))) # [5,4,3,2,1]
    print(Solution().reverseList(head = listtollist([1,2]))) # [2,1]
    print(Solution().reverseList(head = listtollist([]))) # []