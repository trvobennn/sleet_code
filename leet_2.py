
class Solution:

    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for ind, num in enumerate(nums):
            if num != ind:
                return ind
        return len(nums)

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return []
        unique_nums = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in unique_nums]
