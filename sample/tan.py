class Solution:
    def are(self,k):
        marr=0
        n=len(k)
        sl=[-1]*n
        d=[]
        for i in range(n):
            while d and k[d[-1]]>=k[i]:
                d.pop()
            if d:
                sl[i]=d[-1]
            d.append(i)
        d=[]
        rl=[n]*n
        for i in range(n-1,-1,-1):
            while d and k[d[-1]]>=k[i]:
                d.pop()
            if d:
                rl[i]=d[-1]
            d.append(i)
        for i in range(n):
            marr=max(marr,(k[i]*(rl[i]-sl[i]-1)))
        return marr

    def maximalRectangle(self, matrix) -> int:
        m,n=len(matrix),len(matrix[0])
        k=[]
        for i in matrix[0]:
            k.append(int(i))
        print(k)
        minA=self.are(k)
        for i in range(1,len(matrix)):
            k=[x + int(y) for x, y in zip(k,matrix[i])]
            print(k,i)
            minA=max(minA,self.are(k))
        return minA
l=Solution()
print(l.maximalRectangle([["1","0"],["0","1"]]))        













