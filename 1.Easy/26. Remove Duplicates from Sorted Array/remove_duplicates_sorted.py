from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_array = []
        for num in nums:
            if num not in unique_array:
                unique_array.append(num)
        
        for i in range(len(nums)):
            if i < len(unique_array):
                nums[i] = unique_array[i]
            else:
                nums[i] = '_'
        
        return len(unique_array)


if __name__ == "__main__":
    # Example 1
    nums1 = [1, 1, 2]
    solution = Solution()
    k1 = solution.removeDuplicates(nums1)
    print(f"Example 1: k = {k1}, nums = {nums1[:k1]}")

    # Example 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(f"Example 2: k = {k2}, nums = {nums2[:k2]}")
