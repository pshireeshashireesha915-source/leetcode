class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s=sorted(s)
            t=sorted(t)
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
                    break
            else:
                return True    

        