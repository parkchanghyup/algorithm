def maxSubArray( nums: List[int]) -> int:
    for i in range(1,len(nums)):
        nums[i] +=nums[i-1] if nums[i-1]>0 else 0
    return max(nums)
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)