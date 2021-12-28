''' 비효율적인 코드
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx,num in enumerate(numbers):    
            if target - num not in numbers:
                continue
            index= bisect.bisect_left(numbers,target-num,idx+1)
            
            if num+numbers[index]==target:
                return [idx+1,index+1]
'''




class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx,num in enumerate(numbers):    
                
            index= bisect.bisect_left(numbers,target-num,idx+1)
            
            if index < len(numbers) and num+numbers[index]==target:
                return [idx+1,index+1]