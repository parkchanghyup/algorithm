class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        strs = re.sub(r'[^\w]', ' ', paragraph)
        strs = [s for s in strs.lower().split() if s not in banned]
        counts = collections.Counter(strs)
        return counts.most_common(1)[0][0]