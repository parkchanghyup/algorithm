class Solution:
    def groupAnagrams( self,strs: List[str]) -> List[List[str]]:
        dic  = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            dic[key].append(s)
    
        return dic.values()
        