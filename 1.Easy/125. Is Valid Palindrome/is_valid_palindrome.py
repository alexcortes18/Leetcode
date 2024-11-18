class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_string = "".join(char for char in s if char.isalnum()).lower()
        if alphanum_string == "": return True

        # Both odd and even numbered strings need the same case.
        # 'bob', we need to check stop_index = 1, not including index 1 ('o')
        # 'baba', we need to check stop_index = 2, until half the string.
        stop_index = len(alphanum_string)//2 
        for i in range(stop_index):
            if alphanum_string[i] != alphanum_string[-i-1]:
                return False
        return True