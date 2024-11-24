# import time

class Solution:
    def isHappy(self, n: int) -> bool:
        digits, cycling_numbers = [], []
        cycling_numbers.append(n)
        if n==1: return True
        while n != 1:
            # Get the digits of the number n.
            while n > 0:
                digits.append(n%10)
                n = n//10
                
            # Sum the digits and get a new number n.
            n = sum([x**2 for x in digits])
            digits = []
            
            if n == 1: return True
            if n not in cycling_numbers:
                cycling_numbers.append(n)
            else: return False

if __name__ == "__main__":
    solution = Solution()
    
    solution.isHappy(2)