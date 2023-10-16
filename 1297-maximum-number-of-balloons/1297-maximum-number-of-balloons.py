from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = Counter("balloon")  # requirements dict
        text_dict = Counter(text)  # Counter dict

        # Calculate max ballons
        res = float('inf')
        for letter in balloon_dict:
           res = min(res,text_dict[letter] // balloon_dict[letter])
        return res