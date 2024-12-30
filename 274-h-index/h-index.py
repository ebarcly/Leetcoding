class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # easy approach: less optimal O(n log n)
        # will improve to O(n) using extra spac
        
        citations.sort(reverse=True)
        
        for i in range(len(citations)):
            papers = i + 1
            if papers > citations[i]:
                return papers - 1
            if papers == citations[i]:
                return papers
        return papers