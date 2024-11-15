class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        len_n = len(needle)
        len_h = len(haystack)

        for i in range(len_h-len_n+1):
            if haystack[i:i+len_n] == needle:
                return i
        return -1
    
if __name__ == "__main__":
    needle = "sad"
    haystack = "eeesadholasad"
    
    solution = Solution()
    
    index = solution.strStr(haystack, needle)
    print(f"First index found was: {index}")