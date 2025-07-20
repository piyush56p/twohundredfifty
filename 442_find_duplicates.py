class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for num in nums:
            freq = hashmap.get(num, 0) + 1
            hashmap[num] = freq
        for k, v in hashmap.items():
            if v>1:
                res.append(k)
        return res
        
        
