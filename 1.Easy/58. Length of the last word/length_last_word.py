class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        length = 0
        for i in range(len(s)):
            if s[-i-1] != " ":
                length+=1
            else:
                break
        return length


if __name__ == '__main__':
    # Example 1
    s1 = "Hello World"
    solution = Solution()
    result1 = solution.lengthOfLastWord(s1)
    print(f"Input: '{s1}' -> Length of last word: {result1}")

    # Example 2
    s2 = "   fly me   to   the moon  "
    result2 = solution.lengthOfLastWord(s2)
    print(f"Input: '{s2}' -> Length of last word: {result2}")

    # Example 3
    s3 = "luffy is still joyboy"
    result3 = solution.lengthOfLastWord(s3)
    print(f"Input: '{s3}' -> Length of last word: {result3}")

    # Example 4
    s4 = "a"
    result4 = solution.lengthOfLastWord(s4)
    print(f"Input: '{s4}' -> Length of last word: {result4}")
