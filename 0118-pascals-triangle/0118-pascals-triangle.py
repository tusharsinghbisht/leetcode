class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2: 
            return [[1], [1, 1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            res_i = [1]*(i+1)
            prev = res[i-1]
            for j in range(1, i):
                res_i[j] = prev[j-1] + prev[j]

            res.append(res_i)

        return res 