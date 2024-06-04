def par(size,res,n,n1,n2):
    if n2>n1:
        return
    if n%2!=0:
        print("Not possible")
        return
    if size==n:
        if n1==n2:
            print(res)
        return
    par(size+1,res+"(",n,n1+1,n2)
    # if n2>n1:
    #     return
    par(size+1,res+")",n,n1,n2+1)

n=int(input())
par(0,"",n,0,0)
