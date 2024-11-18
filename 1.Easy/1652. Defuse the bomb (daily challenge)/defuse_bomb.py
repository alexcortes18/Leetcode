from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:    
        # Works but Too unnecessarily complex and repetitive.
        # result = []    
        # if k == 0:
        #     return [0] * len(code)
        # if k > 0:
        #     new_code = code + code[0:k]
        #     for i in range(len(code)):
        #         sum_ = 0
        #         for j in range(k):
        #             sum_ +=  new_code[i + j + 1]
        #         result.append(sum_)
        # if k < 0 :
        #     new_code = code[k:] + code
        #     for i in range(len(code)):
        #         sum_ = 0
        #         for j in range(-k):
        #             sum_ += new_code[-k+i-j-1]
        #         result.append(sum_)
        # return result

        # Better option:
        # use sum(code[i+1:i+1+k])
        result = []
        if k == 0:
            return [0] * len(code)
        if k > 0:
            new_code = code + code[:k]
            for i in range(len(code)):
                result.append(sum(new_code[i+1:i+1+k]))
        if k < 0:
            new_code = code[k:] + code
            for i in range(len(code)):
                result.append(sum(new_code[i:i-k])) #because k is negative
        return result
