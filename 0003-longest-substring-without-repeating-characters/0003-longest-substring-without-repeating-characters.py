class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     a=[]
     m = 0
     for i in s:
            if i not in a:
                a.append(i)
            else:
                m=max(m,len(a))
                while i in a:
                    a.pop(0)
                a.append(i)
     m=max(m,len(a))
     return m

        