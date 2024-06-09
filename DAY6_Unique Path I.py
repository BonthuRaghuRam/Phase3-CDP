class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache=[]
        for i in range(m):
            row=[-1]*n
            cache.append(row)
        def recursiveApproach(row,col):
            if row==m-1 and col==n-1:
                return 1
            elif row==m or col==n:
                return 0
            elif cache[row][col]!=-1:
                return cache[row][col]
            downWay=recursiveApproach(row+1,col)
            rightWay=recursiveApproach(row,col+1)
            cache[row][col]=downWay+rightWay
            return cache[row][col]
        return recursiveApproach(0,0)
        def tabulationApproach():
            cache=[]
            for i in range(m+1):
                row=[0]*(n+1)
                cache.append(row)
            cache[m-1][n-1]=1
            for row in range(m-1,-1,-1):
                for col in range(n-1,-1,-1):
                    if row==m-1 and col==n-1:
                        continue
                    downWay=cache[row+1][col]
                    rightWay=cache[row][col+1]
                    cache[row][col]=downWay+rightWay
            return cache[0][0]
        return tabulationApproach()
