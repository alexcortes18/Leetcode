from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Solution 1 -> O(n)
        # returned_index = 0
        # if target > nums[-1]: return len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == target or nums[i] > target:
        #         return i

        # Solution 2 -> O(log(n))
        # if target > nums[-1]: return len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:  # Target found
                return mid
            elif nums[mid] > target:  # Target is in the left half
                right = mid - 1
            else:  # Target is in the right half
                left = mid + 1

        # At this point, `left` is the insertion index
        return left

if __name__ == '__main__':
    solution = Solution()

    # Example 1
    nums1 = [1, 3, 5, 6]
    target1 = 5
    result1 = solution.searchInsert(nums1, target1)
    print(f"Example 1: nums = {nums1}, target = {target1}, result = {result1}")

    # Example 2
    nums2 = [1, 3, 5, 6]
    target2 = 2
    result2 = solution.searchInsert(nums2, target2)
    print(f"Example 2: nums = {nums2}, target = {target2}, result = {result2}")

    # Example 3
    nums3 = [1, 3, 5, 6]
    target3 = 7
    result3 = solution.searchInsert(nums3, target3)
    print(f"Example 3: nums = {nums3}, target = {target3}, result = {result3}")

    # Additional Example
    nums4 = [1, 3, 5, 6]
    target4 = 0
    result4 = solution.searchInsert(nums4, target4)
    print(f"Additional Example: nums = {nums4}, target = {target4}, result = {result4}")
