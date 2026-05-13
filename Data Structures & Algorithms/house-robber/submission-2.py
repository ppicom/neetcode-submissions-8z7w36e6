class Solution:
    """
    Intuition
    The recursive solution recomputes the same subproblems many times.
    To optimize this, we store the result for each index once it’s computed.

    At every house i, you still have two choices:

    Skip the house → go to i + 1
    Rob the house → take nums[i] and go to i + 2
    Using memoization, each index is solved only once.
    """
    def rob(self, nums: List[int]) -> int:
        memo = [-1] *len(nums)

        def dfs(i):
            if i>=len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        
        return dfs(0)
