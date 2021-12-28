class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        min_num  =min(nums)
        index = nums.index(min_num)
        nums.sort()
        idx = bisect.bisect_left(nums,target)


        return (idx+index)%len(nums)