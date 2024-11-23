class Solution:
    def hammingWeight(self, n: int) -> int:
        string_bits = bin(n)[2:]
        output = 0
        for bit in string_bits:
            output += 1 if int(bit) == 1 else 0
        
        return output