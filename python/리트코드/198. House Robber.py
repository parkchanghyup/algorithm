class Solution:
    def rob(self,nums: List[int]) -> int:
        if len(nums) ==0 : 
            return 0
        if len (nums) <=2:
            return max(nums)
        
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-1],nums[i]+nums[i-2])
        return max(nums)