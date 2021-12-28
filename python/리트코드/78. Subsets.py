class Solution:
    def subsets(self,nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(len(nums)+1):
            comb = list(itertools.combinations(nums,i))
            for j in range(len(comb)):
                results.append(list(comb[j]))
        return results