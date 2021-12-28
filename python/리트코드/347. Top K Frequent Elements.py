class Solution
    def topKFrequent(self, nums List[int], k int) - List[int]
        a = collections.Counter(nums)
        result =[]
        for _ in a.most_common(k)
            result.append(_[0])
        return result
