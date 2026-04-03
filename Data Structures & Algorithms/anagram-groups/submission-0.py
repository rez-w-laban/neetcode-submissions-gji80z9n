class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            ii = "".join(sorted(i))
            if ii not in d:
                d[ii] = []
            d[ii].append(i)
        return list(d.values())
        

        



        