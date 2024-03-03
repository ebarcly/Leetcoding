class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Create two maps (Mapping letters to words and words to letters using dictionary is a straight fordward approach to solve this problem).
        charToWords, wordsToChar = {}, {}

        # Get an array of the words without spaces (clean the words of spaces)
        strArray = s.split(" ")
        # Check if the lengths are equal, if not equall they cannot follow the same pattern (number of characters should be equal number of words for this to work).
        if len(pattern) != len(strArray):
            return False

        # Loop through the char in string and words in array simultaneously:
        for char, word in zip(pattern, strArray):
            # if either mapping does not match their corresponding assignment then the result is false.
            if (char in charToWords and word != charToWords[char]) or (
                word in wordsToChar and char != wordsToChar[word]
            ):
                return False
            charToWords[char] = word
            wordsToChar[word] = char
        return True
