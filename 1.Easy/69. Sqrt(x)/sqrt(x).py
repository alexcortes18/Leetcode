class Solution:
    def mySqrt(self, x: int) -> int:
        # slow way:
        # i = 1
        # nearest_square = 0
        # while i * i <= x:
        #     nearest_square = i
        #     i += 1
        # return nearest_square

        if x == 0:  # Handle edge case where x is 0
            return 0

        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid  # Found exact square root
            elif mid * mid < x:
                low = mid + 1  # Move to the right half
            else:
                high = mid - 1  # Move to the left half

        # If no exact square root, return the largest integer less than sqrt(x)
        return high



if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [0, 1, 4, 8, 10, 15, 16, 25, 100]
    for x in test_cases:
        print(f"The integer square root of {x} is: {solution.mySqrt(x)}")
