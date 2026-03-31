class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * (2 * l)
        for i in range(0, l):
            ans[i] = nums[i]
            ans[l+i] = nums[i]
        return ans