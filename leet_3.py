
class Solution:

    def singleNumber(self, nums: list[int]) -> int:
        memo={}
        for n in nums:
            memo[n] = memo[n] + 1 if n in memo else 1

        for n in memo:
            if memo[n] == 1:
                return n


    def climbStairs(self, n: int, memo=None) -> int:
        # climb in increment of 1 or 2 steps
        # how many unique ways can a set of n stairs be climbed
        # start memo
        # if n in memo return memo[n]
        # have counter of paths add if return is not none
        # if n == 0 return counter
        # if n < 0 return None
        # loop through step increments and run recursion
        # memo[n] = climbStairs(stairs_left - 1,memo) + climbStairs(stairs_left - 2, memo)
        # return memo[n]
        if memo is None:
            memo = {}
        if n in memo: return memo[n]
        p_counter = 0
        if n == 0:
            p_counter += 1
            return p_counter
        if n < 0: return 0
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]
