class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            cur = nums[i]
            dif = target - cur
            if cur in seen:
                return [seen[cur], i]
            else:
                seen[dif] = i
        return []