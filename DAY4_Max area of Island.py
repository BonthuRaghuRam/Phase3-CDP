class Solution:
    def dfs(self,grid,i,j,res):
        if not grid:
            return 0
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
            return
        res[0]+=1
        grid[i][j]=0
        self.dfs(grid,i-1,j,res)
        self.dfs(grid, i + 1, j, res)
        self.dfs(grid, i, j-1, res)
        self.dfs(grid, i, j+1, res)
        return res
    def maxAreaOfIsland(self, grid):
        res=[0]
        maxArea=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res[0]=0
                    res=self.dfs(grid,i,j,res)
                    maxArea=max(maxArea,res[0])
        return maxArea

        
