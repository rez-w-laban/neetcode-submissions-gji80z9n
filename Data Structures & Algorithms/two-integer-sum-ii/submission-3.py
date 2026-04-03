class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers) - 1
        
        while numbers[i] + numbers[j] != target :
            sum = numbers[i] + numbers[j]
            if sum > target:
                j -=1
            elif sum < target:
                i +=1
           

        return [i+1,j+1]


        