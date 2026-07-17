class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i in"({[":
                l.append(i)
            else:
                if len(l)!=0:
                    if i ==")" and l[-1]!="(":
                        return False
                    elif i =="]" and l[-1]!="[":
                        return False
                    elif i =="}" and l[-1]!="{":
                        return False
                    l.pop()
                else:
                    return False
        if len(l) == 0:
            return True
        else:
            return False
        
        