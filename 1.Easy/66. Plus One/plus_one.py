from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # MINE:
        # string_number = ''
        # for integer in digits:
        #     string_number += str(integer)
        # plus_one = int(string_number) + 1

        # final_array_digits = []
        # for char in str(plus_one):
        #     final_array_digits.append(int(char))
        # return final_array_digits

        # CHATgpt:
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1

            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        #if it finished the loop, it carried the one all the way through:
        return [1] + digits
    
if __name__ == "__main__":
    # Test Case 1
    digits1 = [1, 2, 3]
    solution = Solution()
    print(f"Input 1: {digits1}")
    result1 = solution.plusOne(digits1)
    print(f"Output 1: {result1}")

    # Test Case 2
    digits2 = [4, 3, 2, 1]
    print(f"Input 2: {digits2}")
    result2 = solution.plusOne(digits2)
    print(f"Output 2: {result2}")

    # Test Case 3
    digits3 = [9, 9, 9]
    print(f"Input 3: {digits3}")
    result3 = solution.plusOne(digits3)
    print(f"Output 3: {result3}")

    # Test Case 4
    digits4 = [0]
    print(f"Input 4: {digits4}")
    result4 = solution.plusOne(digits4)
    print(f"Output 4: {result4}")