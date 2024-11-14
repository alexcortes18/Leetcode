from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # MINE:
        # concatenated = ''
        # min_string = strs[0]
        # for i in range(len(strs)):
        #     if(len(strs[i]) <= len(min_string)):
        #         min_string = strs[i]

        # for j in range(len(min_string)):
        #     for i in range(len(strs)):
        #         if(i == len(strs)-1):
        #             concatenated += strs[i][j]
        #             break
        #         if(strs[i][j] != strs[i+1][j]):
        #             return concatenated
        # return concatenated
        
        
        # --------------------------
        # CHATgpt:
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # Keep reducing the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""  # If there's no common prefix, return an empty string
        
        return prefix

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["apple", "applause", "apricot"], "ap"),
        (["cat", "car", "cab"], "ca"),
        (["interview", "internet", "intermediate"], "inter")
    ]
    
    # Loop through test cases and print the result
    for strs, expected in test_cases:
        result = solution.longestCommonPrefix(strs)
        print(f"For input {strs}, the longest common prefix is: \"{result}\" Expected: \"{expected}\"")