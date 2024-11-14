from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # My previous code
        # smaller_array = []
        # for i in range(len(nums)):
        #     if(nums[i] != val):
        #         smaller_array.append(nums[i])

        # for i in range(len(nums)):
        #     if(i < len(smaller_array)):
        #         nums[i] = smaller_array[i]
        #     else:
        #         nums[i] = ''
        # return len(smaller_array)
        
        # Chatgpt better way. I understand it.
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(f'After: {nums}')
        return k
    
if __name__ == '__main__':
    # Example 1:
    nums1 = [3, 2, 2, 3]
    val1 = 3 # value to remove
    solution = Solution()
    k1 = solution.removeElement(nums1, val1)
    print(f"Example 1: k = {k1}, nums = {nums1[:k1]}")

    # Example 2:
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2 # value to remove
    k2 = solution.removeElement(nums2, val2)
    print(f"Example 2: k = {k2}, nums = {nums2[:k2]}")
