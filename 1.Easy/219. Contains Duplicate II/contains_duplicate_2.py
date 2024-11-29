from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # comparing_list = []
        # for i, num in enumerate(nums):
        #     if num not in comparing_list:
        #         comparing_list.append(num)
        #     else:
        #         original_num_index = comparing_list.index(num)
        #         if k >= abs(original_num_index - i): return True
        #         comparing_list[original_num_index] = None
        #         comparing_list.append(num)
        # return False

        # sliding_list = []
        # for i, num in enumerate(nums):
        #     if i+k+1 <= len(nums):
        #         sliding_list = nums[i:i+k+1]
        #     else: 
        #         sliding_list = nums[i:]

        #     for j in range(len(sliding_list)):
        #         for z in range(j+1, len(sliding_list)):
        #             # print("Values of j and z:",j," ",z)
        #             # print("Nums are: ", sliding_list[j]," ",sliding_list[z])
        #             if sliding_list[j] == sliding_list[z] and \
        #              abs(j-z) <= k: return True
        # return False

        #ChatGPT solution
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
                
    
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic example with duplicates within range k
    nums = [1, 2, 3, 1]
    k = 3
    print("Test Case 1:", solution.containsNearbyDuplicate(nums, k))  # Expected: True

    # Test case 2: Duplicates exist but are out of range
    nums = [99,99]
    k = 2
    print("Test Case 2:", solution.containsNearbyDuplicate(nums, k))  # Expected: True

    # Test case 3: No duplicates in the list
    nums = [1, 2, 3, 4, 5]
    k = 2
    print("Test Case 3:", solution.containsNearbyDuplicate(nums, k))  # Expected: False
