from typing import List


class Solution:
    def bruteForce(self, nums: List[int]) -> int:
        """
        O(n^3)
        """
        max_sum = float("-inf")

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = 0
                for k in range(i, j + 1):
                    total += nums[k]
                if total > max_sum:
                    max_sum = total

        return max_sum

    def bitBetter(self, nums: List[int]) -> int:
        """
        O(n^2)
        """
        max_sum = float("-inf")

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total > max_sum:
                    max_sum = total

        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Kadane's algo - O(n)
        max_sum = float("-inf")
        total = 0

        for num in nums:
            total += num

            if total > max_sum:
                max_sum = total

            # if the total drops below zero, no point in carrying this forward since we want
            # to maximize the total total
            if total < 0:
                total = 0

        return max_sum
