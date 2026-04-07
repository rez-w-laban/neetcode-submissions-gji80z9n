class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack 
        stack = []
        res=[0] * len(temperatures)
    
        for i , j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                temp,indx = stack.pop()
                res[indx] = i - indx
            stack.append((j,i))
        
        
        return res




    

        