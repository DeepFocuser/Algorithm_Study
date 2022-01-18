from re import M
from typing import List
from collections import deque

# 1. 양쪽에서 구하기 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left, right = 0, len(nums)-1
        front = deque()
        back = deque()
        result = [-1,-1]

        # [5,7,7,8,8,10]
        while left < len(nums) or right > -1:

            if nums[left] == target:
                front.append(left)
            left +=1

            if nums[right] == target:
                back.append(right)
            right-=1

            if front and back:
                break
        
        if front and back:
            result = [front.popleft(), back.popleft()] 

        return result

# 2. 이진탐색 3개 이용 / 일반적인 이진탐색으론 불가능 / 이진탐색은 뭐 오름차순 정렬이 기본임
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # nums가 빈 리스트인 경우 [-1,-1] 반환
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums)-1
        middle = len(nums)-1

        front = deque()
        back = deque()

        # [1,2,3,4,5,6]
        # 입력 예시 : [5,7,7,8,8,10]
        # 입력 예시 : [7,8,8,8,8,8]
        # 1. target 값 찾기 
        while left <= right:
            middle = (left + right)//2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                front.append(middle)
                back.append(middle)
                break
        
        # 2. 처음 인덱스와 마지막 인덱스가 존재하는 경우에만 수행
        if front and back:
            middle_for_left = middle
            middle_for_right = middle
            left = 0
            # (1). middle을 기준으로 왼쪽으로 가보기(최대 인덱스및 중복 처리) 
            while left < middle_for_left:
                leftmiddle = (left + middle_for_left) // 2
                if nums[leftmiddle] < target:
                    left = leftmiddle + 1
                elif nums[leftmiddle] == target:
                    front.append(leftmiddle)
                    middle_for_left = leftmiddle

            # (2). middle을 기준으로 오른쪽으로 가보기(최대 인덱스 및 중복 처리)
            right = len(nums)-1
            while middle_for_right <= right:
                rightmiddle = (middle_for_right + right) // 2
                if nums[rightmiddle] > target:
                    right = rightmiddle - 1
                elif nums[rightmiddle] == target:
                    back.append(rightmiddle)
                    middle_for_right = rightmiddle + 1

            return [front.pop(), back.pop()]
        
        return [-1, -1]


if __name__ == "__main__":

    '''
    Given an array of integers nums sorted in non-decreasing order, 
    find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
 
    Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
    
    '''
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)) # [3,4]
    # print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6)) # [-1,-1]
    # print(Solution().searchRange(nums = [8,8,8,8,8,8], target = 8)) # [0,5]
    # print(Solution().searchRange(nums = [], target = 0)) # [-1,-1]
    # print(Solution().searchRange(nums = [2,2], target = 3)) # [-1,-1]
    # print(Solution().searchRange(nums = [1], target = 1)) # [0, 0]
    # print(Solution().searchRange(nums = [1,3], target = 1)) # [0, 0]