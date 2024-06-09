from typing import List


class Solution:
    def reverseArray(self, array: List[int], start_idx: int, end_idx: int):
        """
        Reverses a sub-array of an array in-place, startIndex and endIndex both inclusive
        """
        while start_idx < end_idx:
            array[start_idx], array[end_idx] = array[end_idx], array[start_idx]
            start_idx += 1
            end_idx -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Example:
        nums [2, 1, 5, 4, 3, 0, 0]
        - breaking point at index (1) the nums are 1, 5
        - find a num bigger than breaking point num (1) with minimum distance from it (in this case 3)
        - swap the num 1 and 3 to get [2, 3, 5, 4, 1, 0, 0]
        - reverse all nums upto the breaking point [5, 4, 1, 0, 0] to get the lowest num sequence, since a
          bigger num (3) was already placed in position
        """
        len_nums = len(nums)

        # first going to check the breaking point (breaking point is a num smaller than it's next num)
        breaking_point = -1
        for i in range(len_nums - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                breaking_point = i
                break

        # if no breaking point is found then the array is in descending order
        # so just return the reversed array
        if breaking_point == -1:
            self.reverseArray(nums, 0, len_nums - 1)
            return

        # find a num bigger than breaking point num, with minimum distance from it
        # swap this num with the breaking point num
        # because the nums were in descending order, just find the first num that is bigger than breaking point num
        for i in range(len_nums - 1, breaking_point, -1):
            if nums[i] > nums[breaking_point]:
                nums[i], nums[breaking_point] = nums[breaking_point], nums[i]
                break

        # reverse the nums from breaking point to the end
        self.reverseArray(nums, breaking_point + 1, len_nums - 1)
