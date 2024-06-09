class Solution:
    def minimizeCost(self, height, n, k):
        cache=[-1]*n  #Exclude line 3,7,8,16 to make it as Recursive one
        def memoizationApproach(index):
            if index==n-1:
                return 0
            if cache[index]!=-1:
                return cache[index]
            result=1000000000
            for i in range(1,k+1):
                nextIndex=index+i
                if nextIndex>=n:
                    break
                currRes=abs(height[index]-height[nextIndex])+recursionApproach(nextIndex)
                result=min(result,currRes)
            cache[index]=result
            return result
        return recursionApproach(0)
        def tabulationApproach():
            cache[n-1]=0
            for index in range(n-2,-1,-1):
                result=1000000000
                for i in range(1,k+1):
                    nextIndex=index+i
                    if nextIndex>=n:
                        break
                    currRes=abs(height[index]-height[nextIndex])+cache[nextIndex]
                    result=min(result,currRes)
                cache[index]=result
            # print(cache)
            return cache[0]
        return tabulationApproach()
