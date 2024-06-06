def pathway(x,y,matrix,path,res,visited):
    if x<0 or x>=len(matrix) or y<0 or y>=len(matrix) or matrix[x][y]==0 or visited[x][y]==True:
        return
    if x==len(matrix)-1 and y==len(matrix)-1:
        res.append(path[:])
        return
    path.append(1)
    visited[x][y] = True
    pathway(x - 1, y, matrix, path,res, visited)
    pathway(x + 1, y, matrix,path,res, visited)
    pathway(x, y - 1, matrix, path, res, visited)
    pathway(x, y + 1, matrix, path, res, visited)
    path.pop()
    visited[x][y] = False


matrix=[[1,0,0,0],
        [1,1,0,1],
        [0,1,1,0],
        [0,1,1,1]]
path=[]
res=[]
visited=[]
for i in range(len(matrix)):
    eachRow=[]
    for j in range(len(matrix[0])):
        eachRow.append(False)
    visited.append(eachRow)
pathway(0,0,matrix,path,res,visited)
print(res)
if len(res)>=1:
    print(True)
else:
    print(False)
