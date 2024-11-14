class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0): return False
        if(len(str(x))==1): return True
        # if(len(str(x))%2==0): return False

        half_length = int(len(str(x))/2)
        string_number = str(x)

        for i in range(half_length):
            if(string_number[i] != string_number[-i-1]):
                return False
        return True
    
if __name__ == "__main__":
    solution = Solution()
    # Test cases
    test_cases = [121, -121, 10, 12321, 123321, 0, 7]
    
    for num in test_cases:
        result = solution.isPalindrome(num)
        print(f"Is {num} a palindrome? {result}")
