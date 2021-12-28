class Solution:

    def numJewelsInStones(self, J : str,S:str)-> int:
        count = 0
        freqs = collection.Counter(S) # 돌 빈도수 계산

        # 비교 없이 보석 J 빈도수 계산
         for char in J:
            count +=freqs[char] 

        return count
