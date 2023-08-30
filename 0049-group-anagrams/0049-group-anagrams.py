class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a hashmap to store the key:value pairs
        anagrams = {}

        # iterate through each word in the list
        for word in strs:
            sorted_word = ''.join(sorted(word))  # sort the words to use the as key in the dict
            # check if the sorted word is in the dict
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]  # if not, add it in the dict as a key
            else:
                anagrams[sorted_word].append(word)  # if it is, appended to the list of words

        # return a list of the values in the dictionary
        return list(anagrams.values())