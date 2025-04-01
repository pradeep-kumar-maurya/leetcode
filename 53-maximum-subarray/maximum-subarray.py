class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):

            if sum <= 0 and nums[i] > 0:
                sum = nums[i]

            elif sum > 0 and sum + nums[i] < 0:
                sum = 0

            elif sum < 0 and nums[i] > sum:
                sum = nums[i]

            else:
                sum += nums[i]

            if sum > max_sum:
                max_sum = sum

        return max_sum

        