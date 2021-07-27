# REF https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(nums):
            for j in range(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
