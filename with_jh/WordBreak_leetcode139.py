from typing import List

# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass 

if __name__ == "__main__":

    Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"]) # true
    Solution().wordBreak(s = "applepenapple", wordDict = ["apple","pen"]) # true
    Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]) # false


