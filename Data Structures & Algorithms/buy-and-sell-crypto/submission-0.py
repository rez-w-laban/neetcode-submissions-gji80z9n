class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices)) : 
            for j in range(0,i):
                prof = max(prof, prices[i] - prices[j])
        return prof
          
        
        