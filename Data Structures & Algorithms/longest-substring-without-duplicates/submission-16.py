class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        l = []
        if len(s) == 0 :
            return 0
         

        while i < len(s) :
            
            ss = set()
            ss.add(s[i])
            count = 1
            j = i + 1
            while j < len(s) :
                if s[j] in ss:
                    break
                count += 1
                ss.add(s[j])
                j +=1
            l.append(count)
            i +=1
        return max(l)

        

        