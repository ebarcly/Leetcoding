class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {'()', '[]', '{}'}

        for c in s:
            if c in '([{':
                stk.append(c)
            elif not stk or stk.pop() + c not in pairs:
                return False
        
        return not stk