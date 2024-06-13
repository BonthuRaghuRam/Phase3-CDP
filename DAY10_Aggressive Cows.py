
class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        minimum=stalls[1]-stalls[0]
        maximum=stalls[n-1]-stalls[0]
        for i in range(1,n):
            minimum=min(minimum,stalls[i]-stalls[i-1])
        def isPossible(val):
            prevCow=0
            cowsCount=k-1
            for s in range(1,n):
                diff=stalls[s]-stalls[prevCow]
                if diff>=val:
                    prevCow=s
                    cowsCount-=1
                    if cowsCount==0:
                        return True
            return False
        left=minimum
        right=maximum
        result=-1
        while left<=right:
            mid=(left+right)//2
            if isPossible(mid):
                result=mid
                left=mid+1
            else:
                right=mid-1
        return result
