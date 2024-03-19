import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1:
            return True
        
        pattern = re.compile(r'[^a-zA-Z0-9]')
        clean_str = pattern.sub('', s).lower()

        return clean_str == clean_str[::-1]