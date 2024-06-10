class Solution:
    def maximalRectangle(self, matrix):
        m, n = len(matrix), len(matrix[0])
        bars = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    bars[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '0':
                    bars[i][j] = 0
                else:
                    bars[i][j] = bars[i - 1][j] + 1
            print(bars)
        res = 0
        print(bars)
        for i in range(m):
            res = max(res, self.findArea(bars[i]))
        return res

    def findArea(self, bar):
        stack = []
        ngel = [-1] * len(bar)

        for i in range(len(bar)):
            while stack and stack[-1][0] >= bar[i]:
                stack.pop()

            if stack:
                ngel[i] = stack[-1][1]

            stack.append((bar[i], i))

        stack = []
        nger = [len(bar)] * len(bar)

        for i in range(len(bar) - 1, -1, -1):
            while stack and stack[-1][0] >= bar[i]:
                stack.pop()

            if stack:
                nger[i] = stack[-1][1]

            stack.append((bar[i], i))
        res = 0
        for i in range(len(bar)):
            res = max(res, (nger[i] - ngel[i] - 1) * bar[i])

        return res
        
m=Solution()
print(m.maximalRectangle([["1","0"],["0","1"]]))