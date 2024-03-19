class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        convert = ''
        for char in s:
            if char.isdigit() or char.isalpha():
                convert += char
        convert = convert.lower()

        left, right = 0, len(convert) - 1
        while left <= right:
            if convert[left] != convert[right]:
                return False

            left += 1
            right -= 1

        return True