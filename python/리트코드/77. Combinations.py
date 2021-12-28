class Solution:
    def combine( self,n: int, k: int) :
        nums=list(range(1,n+1))
        return list(itertools.combinations(nums,k))