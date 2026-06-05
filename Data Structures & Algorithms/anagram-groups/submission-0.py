class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            sorted_word = str(sorted(s))
            ans[sorted_word].append(s)
        
        return list(ans.values())