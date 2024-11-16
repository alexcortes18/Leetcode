class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        first, second = 1, 2
        for _ in range(3, n+1):
            current = first + second
            first, second = second, current
        return second

# Example usage
solution = Solution()
print(solution.climbStairs(4))  # Output: 4
print(solution.climbStairs(3))  # Output: 3
