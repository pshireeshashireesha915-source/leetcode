class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def vignan(x):
            y = sorted(x)
            m = ''.join(y)
            return m
        