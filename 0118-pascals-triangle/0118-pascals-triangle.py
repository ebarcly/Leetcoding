class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([1])
            for j in range(len(res[i-1]) - 1):
                res[i].append(res[i-1][j] + res[i-1][j+1])
            res[i].append(1)
        return res
                
