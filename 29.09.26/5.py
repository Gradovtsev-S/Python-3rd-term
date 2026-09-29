class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        r = nums[0]
        s = nums[0]
        for i in range(1, len(nums)):
            s = max(s + nums[i], nums[i])
            r = max(s, r)
        return r