class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in strs:
            while i[:len(ans)] != ans:
                ans = ans[:-1]
        return ans

