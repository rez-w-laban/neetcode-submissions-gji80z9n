class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1 :
                count +=1
            else:
                l.append(count)
                count = 0
        print(l)
        l.append(count)
        return max(l)
        