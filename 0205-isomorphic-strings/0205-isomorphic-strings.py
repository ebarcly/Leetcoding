class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # create dictionaries to map characters
        table_s = {}
        table_t = {}

        # algorithm to check if charcacters are being mapped with their corresponding char
        for k, v in zip(s,t):
            if k in table_s and table_s[k] != v:  # if the char is in the table with a dif val
                return False  # strings are not isomorphic
            if v in table_t and table_t[v] != k:
                return False
        
            # create mappings if conditions are met
            table_s[k] = v
            table_t[v] = k

        return True