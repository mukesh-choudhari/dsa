from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity : O(nlogn) <sorting> + O(n^2) <finding triplets>
        """

        if len(nums) == 3:
            return [nums] if (nums[0] + nums[1] + nums[2] == 0) else []

        results = []

        # sorting the original array to always get unique triplets without needing a set
        nums = sorted(nums)

        for idx_1 in range(len(nums)):
            if (idx_1 > 0) and (nums[idx_1] == nums[idx_1 - 1]):
                continue

            idx_2 = idx_1 + 1
            idx_3 = len(nums) - 1

            # 2 pointers to go through the elements on the right of idx_1
            while idx_2 < idx_3:
                sum = nums[idx_1] + nums[idx_2] + nums[idx_3]
                if sum < 0:
                    idx_2 += 1  # sorted array and we need to go towards zero, move left pointer inwards
                elif sum > 0:
                    idx_3 -= 1  # sorted array and we need to go towards zero, move right pointer inwards
                else:
                    # found a triplet
                    results.append([nums[idx_1], nums[idx_2], nums[idx_3]])

                    # move both left and right pointers until new values are detected at respective indices
                    idx_2 += 1
                    idx_3 -= 1
                    while (idx_2 < idx_3) and (nums[idx_2] == nums[idx_2 - 1]):
                        idx_2 += 1
                    while (idx_2 < idx_3) and (nums[idx_3] == nums[idx_3 + 1]):
                        idx_3 -= 1

        return results
