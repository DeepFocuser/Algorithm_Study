from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pass

if __name__ == "__main__":
    sol = Solution()
    print(sol.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
    print(sol.mostCommonWord(paragraph = "a.", banned = []))

    '''
    Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
    Output: "ball"

    Input: paragraph = "a.", banned = []
    Output: "a"
    '''
