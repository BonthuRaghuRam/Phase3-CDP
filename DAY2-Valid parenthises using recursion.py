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

alternative:


def printThis(n, result, openOnes, closedOnes):
    if closedOnes > openOnes:
        return
    if openOnes > (n // 2) or closedOnes > (n // 2):
        return
    if len(result) == n:
        print(result)
        return 
 
    printThis(n, result + "(", openOnes + 1, closedOnes)
    printThis(n, result + ")", openOnes, closedOnes + 1)
 
 
n = 6
printThis(n, "", 0, 0)
