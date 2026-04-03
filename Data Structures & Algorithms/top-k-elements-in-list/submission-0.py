class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] +=1
        z = 0
        res = []
        
        sd = sorted(d.items(),  key=lambda item: item[1] , reverse = True)
        
        while z < k :
            res.append(sd[z][0])
            z +=1
        return res
            
