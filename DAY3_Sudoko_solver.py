class Solution:
    def isPossible(self,x,y,board,value):
        for col in range(9):
            if board[x][col]==str(value):
                return False
        for row in range(9):
            if board[row][y]==str(value):
                return False
        topRow=(x//3)*3
        topCol=(y//3)*3
        for i in range(3):
            for j in range(3):
                if board[topRow+i][topCol+j]==str(value):
                    return False
        return True
    def path(self,x,y,board):
        if x==9:
            return True
        nextX,nextY=-1,-1
        if y==8:
            nextX=x+1
            nextY=0
        else:
            nextX=x
            nextY=y+1
        if board[x][y]!=".":
            return self.path(nextX,nextY,board)
        for value in range(1,10):
            if self.isPossible(x,y,board,value)==True:
                board[x][y]=str(value)
                result=self.path(nextX,nextY,board)
                if result==True:
                    return True
                board[x][y]="."
        return False
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.path(0,0,board)
