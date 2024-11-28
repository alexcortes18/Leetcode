class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set_values = set(nums)
        # if len(set_values) == len(nums): return False
        # else: return True
        return (len(nums) > len(set(nums)))