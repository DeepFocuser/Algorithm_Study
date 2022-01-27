from typing import Optional
from listtoLinkedlist import ListNode, listtollist

# 1,2 방법 결국은 같은 방법
# # 1. 가장 단순한 방법 - 값 추출 후 비교
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         val = []
#         while head:
#             val.append(head.val)
#             head=head.next
        
#         if val == val[::-1]:
#             return True
        
#         return False

# # 2. 정방향 역방향 다구하기 - 메모리를 적게 쓰는걸로 나오는데 이유가???
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         forward = []
#         backward = []
#         prev = None

#         while head:
#             forward.append(head.val)
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp

#         while prev:
#             backward.append(prev.val)
#             prev = prev.next

#         if forward == backward:
#             return True
        
#         return False

# 3. 책에 있는 풀이 방식인데, 다중할당(rev, rev.next, slow = slow, rev, slow.next)을 써야한다.
# leetcode에 돌려보니 실제로 빠른것 같지도 않고, 메모리는 적게 먹는다.(눈에 띌정도는 아님)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        reverse = None
        slow = fast = head

        # fast 2칸식 가고, slow 1칸식 가면됨. 
        while fast and fast.next:
            fast = fast.next.next
            
            # 이렇게 한줄씩 풀어쓰는게 좋지 않을까?
            temp = slow.next
            slow.next = reverse
            reverse = slow
            slow = temp

        # 링크드리스트가 홀수길이를 가진 경우 slow 한칸 더 가주기
        if fast:
            slow = slow.next
        

        # reverse, slow의 값이 같아 끝까지 간 경우 reverse, slow는 None값이 출력 됨
        while reverse and reverse.val == slow.val:
            slow, reverse = slow.next, reverse.next
        
        # reverse가 None이면 True, 반대의 경우 False 반환
        return not reverse # or not slow


if __name__ == "__main__":
    #print(Solution().isPalindrome(head = listtollist([1,3,5,7]))) # true
    #print(Solution().isPalindrome(head = listtollist([1,2,3]))) # false
    print(Solution().isPalindrome(head = listtollist([]))) # false