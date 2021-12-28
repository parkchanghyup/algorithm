import collections
from typing import List
class Solution:
    def twoSum( nums: List[int], target: int) -> List[int]:
        # default딕셔너리 생성
        dic = collections.defaultdict(int)
        # 딕셔너리로 변환
        for i ,num in enumerate(nums):
            dic[num]=i



        for i in range(len(nums)):
            if (target - nums[i]) in list(dic):
                # 자기자신 인 경우 제외
                if i == dic[target-nums[i]]:
                    continue
                # 답을 찾은 경우 return
                else :
                    return i,dic[target-nums[i]]

    twoSum(nums = [2,7,11,15], target = 9)
        