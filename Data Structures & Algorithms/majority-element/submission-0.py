class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mj = len(nums) //2
        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1
        
        for i in dic.keys():
            if dic[i] > mj:
                return i 

        