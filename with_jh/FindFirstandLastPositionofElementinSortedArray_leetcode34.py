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
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6)) # [-1,-1]
    print(Solution().searchRange(nums = [], target = 0)) # [-1,-1]
    print(Solution().searchRange(nums = [1], target = 1)) # [0, 0]
    print(Solution().searchRange(nums = [1,3], target = 1)) # [0, 0]