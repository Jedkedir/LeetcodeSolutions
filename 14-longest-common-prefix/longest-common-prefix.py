class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for x in zip(*strs):
            if len(set(x)) == 1:
                ans = ans+x[0]
            else:
                break
        return ans