import collections
from collections import deque
import re
from typing import List

class Solution:

    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        print(s)


if __name__ == "__main__":
    sol=Solution()
    print(sol.reverseString(["h","e","l","l","o"]))
    print(sol.reverseString(["h","a","n","n","a","h"]))
