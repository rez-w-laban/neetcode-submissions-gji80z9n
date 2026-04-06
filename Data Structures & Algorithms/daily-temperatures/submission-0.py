class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #bf
        res = []
        for i in range(len(temperatures)):
            c= 0
            for j in range( i + 1 ,len(temperatures)):
                c +=1
                if temperatures[j] > temperatures[i]:
                    res.append(c)
                    break
                elif j == len(temperatures) -1 :
                    res.append(0)
                    break
            
                
        res.append(0)
        return res


        
        
        
        



