from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i==j): break
                if(nums[i]+nums[j]== target):
                    return [j,i]
                
if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15]  # Example array
    target = 9             # Target sum
    
    nums = [3,11,6,4,9,18]
    target = 15

    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices of the two numbers that add up to the target:", result)

