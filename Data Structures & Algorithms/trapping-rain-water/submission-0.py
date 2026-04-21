class Solution:
    def trap(self, height: List[int]) -> int:
        mxl =[]
        for i in range(len(height)) :
            res = 0 
            for j in range(i):
                res = max(res,height[j])
            mxl.append(res)                
        mxr = []
        for i in range(len(height)-1,-1,-1):
            res = 0
            for j in range(len(height) - 1 , i , -1):
                res = max(res,height[j])
            mxr.append(res)
        
        print(mxl)
        print(mxr)
        l = len(height ) - 1
        summ = 0
        for i in range(len(height)):
            x = min(mxr[l - i],mxl[i])
            s = x - height[i]
            if s > 0 :
                summ += s
        return summ







        


        

        

                               



        
        
        
        
        