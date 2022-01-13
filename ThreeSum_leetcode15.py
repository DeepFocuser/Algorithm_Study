from typing import List
# import itertools
# #시간초과1
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         result = []
#         if len(nums) >= 3:
#             combinations = itertools.combinations(nums, 3)
#
#             for combination in combinations:
#                 if sum(combination) == 0 and sorted(list(combination)) not in result:
#                     result.append(sorted(list(combination)))
#
#         return result

# 시간초과2
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         result = []
#         length = len(nums)
#         if length >= 3:
#             for i in range(length-2):
#                 for j in range(i+1, length-1):
#                     for z in range(j+1, length):
#                         temp = [nums[i],nums[j],nums[z]]
#                         if sum(temp) == 0 and sorted(temp) not in result:
#                             result.append(sorted(temp))
#         return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        length = len(nums)
        if length >= 3:

            # 오름차순 정렬
            nums.sort()
            for i in range(length-2):
                
                # 중복저장을 방지하기 위함
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                left, right = i+1, length-1

                while left < right:
                    
                    # 투포인터 내에서 계산시 중복저장을 방지하기 위함 - 필수
                    if left > i+1 and nums[left-1] == nums[left]: # 왼쪽 값이랑 같은경우
                        left+=1
                        continue
                    if right < length - 1 and nums[right] == nums[right + 1]: # 오른쪽 값과 같은경우
                        right-=1
                        continue

                    condition = nums[i] + nums[left] + nums[right]
                    if condition == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left+=1
                        right-=1
                    elif condition < 0:
                        left+=1
                    elif condition > 0:
                        right-=1

        return result


if __name__ == "__main__":

    sol = Solution()
    print(sol.threeSum(nums = [-1,-1,2,2,-1,-4])) # 좋은 예
    print(sol.threeSum(nums = [1,-1,-1,0]))
    print(sol.threeSum(nums = [3,0,-2,-1,1,2]))
    print(sol.threeSum(nums = [0,0,0,0]))
    print(sol.threeSum(nums = []))
    print(sol.threeSum(nums = [0]))

