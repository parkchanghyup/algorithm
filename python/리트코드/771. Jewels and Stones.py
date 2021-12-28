class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:

        dic = collections.defaultdict(int)
        for s in S:
            dic[s]+=1
        sum =  0; 
        for s in J:
            if s in dic:
                sum+=dic[s] 
        return sum