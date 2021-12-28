class Solution:
    def letterCombinations( self,digits: str) -> List[str]:
        result = []
        if digits =="":
            return ""
        
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}


        def func(idx :int, s :str):
            if len(s) == len(digits) :
                result.append(s)
                return

            for i in (dic[digits[idx]]):
                func(idx+1,s+i)

        func(0,'')
        return result
