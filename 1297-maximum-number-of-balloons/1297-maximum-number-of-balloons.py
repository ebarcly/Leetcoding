from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Get the count of each letter in "balloon"
        balloons = Counter("balloon")

        # Get the count of each letter in the text
        text_dict = Counter(text)

        # Keep track of the maximum number of "balloon"s that can be formed
        max_balloons = float('inf')  # Or len(balloons)

        # Iterate over each letter in "balloon"
        for letter in balloons:
            # For each letter, find how many times we can form the word "balloon"
            # by dividing the count of the letter in the text by the count of the letter in "balloon"
            # Update 'res' with the minimum value obtained
            max_balloons = min(max_balloons, text_dict[letter] // balloons[letter])

        # Return the result which gives the maximum number of instances of the word "balloon" that can be formed
        return max_balloons