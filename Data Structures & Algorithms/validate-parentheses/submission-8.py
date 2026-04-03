class Solution:
    def isValid(self, s: str) -> bool:
        d={}
        d['('] = ')'
        d['{'] = '}'
        d['['] = ']'
        l = []
        for i in s : 
            if i in d : 
                l.append(i)
                print(l)
            elif  len(l) > 0 and i == d[l[-1]] :
                l.pop()
            else : 
                return False
        return len(l) == 0



      