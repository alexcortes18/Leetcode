class Solution:
    def romanToInt(self, s: str) -> int:
        # mine, a lot more redundant:
        count = 0
        numerals_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        for i in range(len(s)):
            letter = s[i]
            if(i == len(s)-1):
                count += numerals_dict[letter]
                break
            if(s[i]=='C'):
                if(s[i+1]=='D' or s[i+1]=='M'): 
                    count-=100
                else: 
                    count+=100; 
                continue
            if(s[i]=='X'):
                if(s[i+1]=='L' or s[i+1]=='C'): 
                    count-=10; 
                else: 
                    count+=10; 
                continue
            if(s[i]=='I'):
                if(s[i+1]=='V' or s[i+1]=='X'):
                    count-=1
                else: 
                    count+=1; 
                continue
            count += numerals_dict[letter]
        return count
        
        # More efficient by ChatGPT:
        
        # numerals_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # count = 0
        # for i in range(len(s)):
        #     # If current value is less than the next value, subtract the current value
        #     if i + 1 < len(s) and numerals_dict[s[i]] < numerals_dict[s[i + 1]]:
        #         count -= numerals_dict[s[i]]
        #     else:
        #         count += numerals_dict[s[i]]
        # return count

# Main entry point for testing the solution
if __name__ == "__main__":
    solution = Solution()
    # Test cases
    test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    
    # Loop through test cases and print the result
    for roman in test_cases:
        print(f"The integer value of {roman} is: {solution.romanToInt(roman)}")
