class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Boyer-Moore Voting Algorithm 2
        """
        cand_1 = 0
        cand_2 = 0
        counter_1 = 0
        counter_2 = 0

        for i in nums:
            if i == cand_1:
                counter_1 += 1 
            elif i == cand_2:
                counter_2 += 1
            elif counter_1 == 0:
                cand_1 = i
                counter_1 = 1
            elif counter_2 == 0:
                cand_2 = i
                counter_2 = 1
            else:
                counter_1 -= 1
                counter_2 -= 1
        
        # validation
        counter_1 = 0
        counter_2 = 0
        for i in nums:
            if i == cand_1:
                counter_1 += 1
            if i == cand_2:
                counter_2 += 1
        majors = []
        if counter_1 > len(nums) / 3:
            majors.append(cand_1)
        if counter_2 > len(nums) / 3 and cand_2 != cand_1:
            majors.append(cand_2)
        return majors
            