class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # might contain: "([{"...
        mapping = {']':'[',')':'(','}':'{'}

        # if(len(s)==1): return False # redundant because of returning False if stack is not empty

        for char in s:
            if char in mapping:
                if(not stack): return False
                if(stack and (stack.pop() != mapping[char])):
                    return False
            else:
                stack.append(char)
        # if after the For loop we still have elements in the stack, then it means there were not sufficient closing elements.
        if(stack): 
             return False

        return True
    
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("()", True),  # Valid
        ("()[]{}", True),  # Valid
        ("(]", False),  # Invalid
        ("([)]", False),  # Invalid
        ("{[]}", True),  # Valid
    ]
    
    # Loop through test cases and print the result
    for s, expected in test_cases:
        result = solution.isValid(s)
        print(f"For input '{s}', isValid returned: {result}. Expected: {expected}")