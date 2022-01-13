import collections
from collections import deque
import re

class Solution:

    # def isPalindrome(self, s: str) -> bool:
    #     pattern = re.compile('\w+')
    #     result = pattern.findall(s)
    #     temp ="".join(result).upper()
    #     return temp[::-1] == temp

    def isPalindrome(self, s: str) -> bool:
        strs: deque = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True



if __name__ == "__main__":
    sol=Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))
