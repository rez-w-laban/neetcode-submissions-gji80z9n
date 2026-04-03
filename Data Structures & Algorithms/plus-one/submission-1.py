class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        z=0
        k = len(digits) -1
        for i in digits:
            z += i * (10**k)
            k -= 1
        z +=1
        print(z)
        l=[]
        i=1
        while z > 0 :
            l.append(z % 10)
            z = z // 10

        return l[::-1]
            

        