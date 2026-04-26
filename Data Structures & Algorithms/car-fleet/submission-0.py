class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        l=[]
        for i in range(len(position)):
            l.append((position[i],speed[i]))
        stack=[]
        for p,s in sorted(l)[::-1]:
            stack.append((target - p)/ s)
            if len(stack) >1 and stack[-1] <= stack[-2] :
                stack.pop() 
        return len(stack)



            


        
