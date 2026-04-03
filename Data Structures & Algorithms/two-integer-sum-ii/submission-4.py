class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(numbers)):
            nb = target - numbers[i]

            if nb in d:
                return [d[nb],i+1]

            d[numbers[i]] = i+1
        return []