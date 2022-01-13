from typing import Optional
from listtoLinkedlist import ListNode, listtollist

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass

if __name__ == "__main__":
    print(Solution().isPalindrome(head = listtollist([1,2,3,4]))) # true
    print(Solution().isPalindrome(head = listtollist([1,2]))) # false