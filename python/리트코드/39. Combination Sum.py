class Solution:

    def combinationSum(self,candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def func(numbers: list, idx: int):

            if sum(numbers) == target:
                result.append(numbers)
                return
            if sum(numbers) > target:
                return

            for i in range(idx, len(candidates)):
                func(numbers + [candidates[i]], i)

        func([], 0)
        return result