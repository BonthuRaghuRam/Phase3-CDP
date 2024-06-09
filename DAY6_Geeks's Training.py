
class Solution:
    def maximumPoints(self, points, n):
        # Code here
        cache=[]
        for i in range(n+1):#extra row for storing prevday
            row=[-1]*(4)
            cache.append(row)
        def recursiveApproach(day,prevDay):
            if day==n:
                return 0
            elif cache[day][prevDay+1]!=-1:
                return cache[day][prevDay+1]
            result=0
            for option in range(3):
                if option != prevDay:
                    currPoints=points[day][option]+recursiveApproach(day+1,option)
                    result=max(result,currPoints)
            cache[day][prevDay+1]=result
            return result
        return recursiveApproach(0,-1)
        def tabulationApproach():
            cache[n][0]=0         
            cache[n][1]=0
            cache[n][2]=0
            for day in range(n-1,-1,-1):
                cache[day][0] = points[day][0] + max(cache[day + 1][1], cache[day + 1][2])
                cache[day][1] = points[day][1] + max(cache[day + 1][0], cache[day + 1][2])
                cache[day][2] = points[day][2] + max(cache[day + 1][0], cache[day + 1][1])
            #print(cache)   
            return max([cache[0][0], cache[0][1], cache[0][2]])
        return tabulationApproach()
