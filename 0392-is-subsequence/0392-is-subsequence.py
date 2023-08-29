class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == 0:
            return True
        if t == 0:
            return False

        pointer_s = 0
        pointer_t = 0

        while pointer_t < len(t) and pointer_s < len(s):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1
        
        return pointer_s == len(s)



