from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return m
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == 0:
                    nums1[j] = nums2[i]
                    break
        nums1.sort()
        
if __name__ == "__main__":
    nums1 = [1, 3, 5, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 6]
    n = 3
    
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 3, 4, 5, 6]
