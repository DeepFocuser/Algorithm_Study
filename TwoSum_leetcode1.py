from typing import List
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []
        for start_index, num in enumerate(nums):
            if target-num in nums[start_index+1:]:
                result = [start_index, start_index+1+nums[start_index+1:].index(target-num)]
                break

        return result

# 더 빠르게 - dict 사용
class Solution2:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = {}
        for index, num in enumerate(nums):
            if target-num in result: # key확인
                return [result[target-num], index]
            result[num] = index # 위의 구문을 통과하지 못한 것은 사전에 저장

if __name__ == "__main__":
    sol = Solution1()
    print(sol.twoSum(nums = [2,7,11,15], target = 9))
    print(sol.twoSum(nums = [3,2,4], target = 6))
    print(sol.twoSum(nums = [3,3], target = 6))
    print(sol.twoSum(nums = [1,3,5,5,7], target = 12))

    print("#########################")

    sol = Solution2()
    print(sol.twoSum(nums = [2,7,11,15], target = 9))
    print(sol.twoSum(nums = [3,2,4], target = 6))
    print(sol.twoSum(nums = [3,3], target = 6))
    print(sol.twoSum(nums = [1,3,5,5,7], target = 12))
