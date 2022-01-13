from typing import List
from collections import defaultdict

# 처음 리스트와 집합을 사용해서 했던 방법
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = []
        # 1. 일단 알파벳 순서대로 정렬 / strs와 순서는 같음
        for str in strs:
            sorted_strs.append("".join(sorted(str)))

        # 2. 유일한 단어 추출(사전)
        unique_strs = set(sorted_strs)

        # 3. 정답을 담을 공간 만들기
        result =[ [] for _ in range(len(unique_strs))]
        
        # 4. 비교후 담기
        for i, sorted_str in enumerate(sorted_strs): # 순서 같음
            for j, unique_str in enumerate(unique_strs): # 중요
                if unique_str == sorted_str: # 유일한 단어와 정렬된 문자가 같은 경우
                    result[j].append(strs[i])

        return result


# dictionary 힌트 얻고 생각한 방법!
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) # 이것을 알아야 한다.
        #sorted_strs = []

        # # 1. 일단 알파벳 순서대로 정렬
        # for str in strs:
        #     sorted_strs.append("".join(sorted(str)))
        #
        # # 2. 사전을 사용하면 이렇게 간단한 것을!!!
        # for i, sorted_str in enumerate(sorted_strs):
        #     result[sorted_str].append(strs[i])

        # 위의 코드를 2줄로!
        for str in strs:
            result["".join(sorted(str))].append(str)

        return list(result.values())

if __name__ == "__main__":
    # strs[i] consists of lowercase English letters.
    sol = Solution2()
    print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams(strs = [""]))
    print(sol.groupAnagrams(strs = ["a"]))

    '''
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Output: [[""]]
    Output: [["a"]]
    '''
