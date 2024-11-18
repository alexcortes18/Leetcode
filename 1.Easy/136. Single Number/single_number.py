from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Correct but slow implementation: 88% people have done it faster.
        # Mine is done in 668 ms.
        # unique_number = []

        # for i in range(len(nums)):
        #     number = nums[i]
        #     if number not in unique_number:
        #         unique_number.append(number)
        #     else:
        #         unique_number.remove(number)
        # return unique_number[0]

        # ChatGPT told me about XOR operator: ^
        # BITWISE:
        # return true if both are not equal: 1 ^ 0: 1
        # return false if both are equal: 0 ^ 0: 0, or 1 ^ 1: 0

        # This beats 36% of people, done in 7 ms.
        unique_number = 0
        for num in nums:
            unique_number ^= num
        return unique_number






        