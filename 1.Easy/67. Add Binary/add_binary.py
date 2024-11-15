class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.zfill(max(len(a),len(b)))
        b = b.zfill(max(len(a),len(b)))

        carry = 0
        result = [0]* len(a)
        for i in range(len(a)-1,-1,-1):
            total = int(a[i]) + int(b[i]) + carry
            if total == 3:
                result[i] = 1
                carry = 1
            elif total == 2:
                result[i] = 0
                carry = 1
            elif total == 1:
                result[i] = 1
                carry = 0
            else:
                result[i] = 0
                carry = 0
        if carry:
            result = [1] + result

        return ''.join(map(str,result))

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    a1 = "1010"
    b1 = "1011"
    print(f"Example 1: {a1} + {b1} = {solution.addBinary(a1, b1)}")
    
    # Example 2
    a2 = "1101"
    b2 = "101"
    print(f"Example 2: {a2} + {b2} = {solution.addBinary(a2, b2)}")
