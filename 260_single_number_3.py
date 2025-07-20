class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n #00110
        diff_bit = 1 #00001

        while not(diff_bit & xor):
            diff_bit = diff_bit << 1 #00010 & 00110

        a, b = 0,0 
        for n in nums:
            if diff_bit & n: #differentating in bucket, 
                a = a^n
            else:
                b = b^n
        return [a,b]

        
