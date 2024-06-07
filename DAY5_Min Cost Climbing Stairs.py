#################################################### using recursion
# def solveit(index,costs,n):
#     if index>=n:
#         return 0
#     jmp1=solveit(index+1,costs,n)
#     jmp2=solveit(index+2,costs,n)
#     return min(jmp1,jmp2)+costs[index]
# costs=[10,15,20]
# n=len(costs)
# option1=solveit(0,costs,n)
# option2=solveit(1,costs,n)
# print(min(option1,option2))
########################################### using memoization
# def solveit(index,costs,n,cache):
#     if index>=n:
#         return 0
#     if cache[index]!=-1:
#         return cache[index]
#     jmp1=solveit(index+1,costs,n,cache)
#     jmp2=solveit(index+2,costs,n,cache)
#     cache[index]=min(jmp1,jmp2)+costs[index]
#     return cache[index]
# costs=[10,15,20]
# n=len(costs)
# cache=[-1]*n
# option1=solveit(0,costs,n,cache)
# option2=solveit(1,costs,n,cache)
# print(min(option1,option2))
##############################################using tabulaztion
# def solveit(costs,n):
#     cache=[-1]*(n+2)
#     cache[n]=0
#     cache[n+1]=0
#     for index in range(n-1,-1,-1):
#         jmp1=cache[index+1]
#         jmp2=cache[index+2]
#         cache[index]=min(jmp1,jmp2)+costs[index]
#     return min(cache[0],cache[1])

# costs=[10,15,20]
# n=len(costs)
# print(solveit(costs,n

###################################################### Alternate Approach

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_stairs = cost[:2]
        for stair in cost[2:]:
            price1 = stair + dp_stairs[-2]
            price2 = stair + dp_stairs[-1]
            dp_stairs.append(
                min(price1, price2)
            )
            
        return min(dp_stairs[-2:])
