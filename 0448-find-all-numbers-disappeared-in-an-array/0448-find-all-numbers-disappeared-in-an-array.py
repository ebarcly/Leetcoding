class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Initialize an empty list to store the results.
        new = []
    
        # Iterate over each number in the list.
        for i in range(len(nums)):
            # Take the absolute value of nums[i] to get the original number
            # (in case it was made negative in a previous iteration).
            number = abs(nums[i])
        
            # If the corresponding position for this number hasn't been marked negative yet,
            # mark it. This step helps us keep track of numbers we've already seen.
            # The number itself acts as an index (hence number-1 because of 0-based indexing).
            if nums[number-1] > 0:
                nums[number-1] = -nums[number-1]
            
        # Now, iterate over the modified list to find positions that are positive.
        # These positions+1 represent numbers that didn't appear in the original list.
        for n in range(len(nums)):
            if nums[n] > 0:
                # Add 1 to convert from 0-based indexing to actual number.
                new.append(n+1)
    
        # Return the list of missing numbers.
        return new
