class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Iterative method
        counter: counts the number of letters before reaching an empty space.
        """
        counter = 0

        for i in range(len(s) -1, -1, -1):
            if s[i] == " ":
                if counter > 0:
                    return counter
                continue
            counter += 1
        return counter 