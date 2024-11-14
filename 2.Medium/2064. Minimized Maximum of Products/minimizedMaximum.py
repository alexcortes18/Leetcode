# Example
# Input: n = 6, quantities = [11,6]
# Output: 3

# My explanation:
# n = 6 -> 6 stores
# quantites = [11,6] -> 11 products of type A, and 6 products of type B

# We have to distribute to all 6 stores the most amount of only ONE type of product while having the max number of each 
# distribution being the least possible.

# Result -> final answer
# Low -> starts at 1
# High -> starts at max(quantities), which means in this case 11.

# Why Binary search from 1 to 11? Because we are trying to find the optimum value from this range, 11 being the worst 
# case scenario with one store receiving ALL products of one specific type, since they can get only 1 product. 
# These would result in max(11,1,1,1,1,2), for example. With 1,1,1,1,2 being the 6 products of  type B being distributed 
# to the other 5 stores. But 11 is too high and we want  to find the lowest amount which can every store have its max 
# efficiency.

from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x):
            stores_needed = 0
            for quantity in quantities:
                stores_needed += math.ceil(quantity/x)
            return stores_needed <= n

        low, high = 1, max(quantities)
        result = high
        while low<= high:
            mid = (low+high)//2
            if can_distribute(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result

if __name__ == "__main__":
    # Example inputs:
    
    n = 6 #number of stores
    quantities = [11,6] # Quantities to distribute
    
    solution = Solution()
    
    result = solution.minimizedMaximum(n,quantities)
    print(f"The minimized maximum is: {result}")