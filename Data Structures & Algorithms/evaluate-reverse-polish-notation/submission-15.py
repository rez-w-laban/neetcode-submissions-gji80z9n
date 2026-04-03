class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums=[]
        
        for i in tokens:  
             
            if i == '+' :
                
                nums.append(nums.pop() + nums.pop())
                 
            elif i == '-' :
                
                b, a = nums.pop(), nums.pop()
                nums.append(a - b)
            elif i == '*' :
                 
                nums.append(nums.pop() * nums.pop())
            elif i == '/' :
                b,a = nums.pop(), nums.pop()
                nums.append(int(a / b))
            else:
                nums.append(int(i))

        return nums[0]
                

            

            
            
        