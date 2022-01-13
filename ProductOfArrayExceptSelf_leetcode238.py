from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [0]*len(nums)

        # 왼쪽 곱 구하기
        for i in range(len(nums)):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i-1]*nums[i-1]

        # 오른쪽 곱 구해서 왼쪽곱과 곱하기
        for i in range(len(nums)-1, -1 , -1):
            if i == len(nums)-1:
                right = 1
            else:
                right=nums[i+1]*right

            # 바로구하기
            left[i] = left[i]*right

        return left


# 답지에 있는 방법
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]*len(nums)

        # 왼쪽 곱 구하기
        left_pad = 1
        for i in range(len(nums)):
            left[i] = left_pad
            left_pad = left_pad * nums[i] # 다음 것 준비 

        # 오른쪽 곱 구해서 왼쪽곱과 곱하기
        right_pad = 1
        for i in range(len(nums)-1, -1 , -1):
            left[i]=left[i]*right_pad
            right_pad = nums[i] * right_pad # 다음 것 준비

        return left

if __name__=="__main__":
    print(Solution().productExceptSelf(nums = [1,2,3,4]))
