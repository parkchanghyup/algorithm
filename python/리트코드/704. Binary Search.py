class Solution:
    def search(sort,nums: List[int], target: int) -> int:

        if target not in nums:
            return -1

        index = bisect.bisect_left(nums,target)
        return index
