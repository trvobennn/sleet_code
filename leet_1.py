
class Solution:

    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for ind, item in enumerate(nums):
            if ind < len(nums)-1 and item == nums[ind+1]:
                return True
        return False

    def containsDuplicate_(self, nums: list[int]) -> bool:
        memo = set(nums)
        if len(memo) < len(nums):
            return True
        return False
