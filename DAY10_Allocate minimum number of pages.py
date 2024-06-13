class Solution:
    def findPages(self,A, N, M):
        if N<M:
            return -1
        left=min(A)
        right=sum(A)
        result=-1
        def isPossible(val):
            student=1
            currSum=0
            for pages in A:
                if pages>val:
                    return False
                elif currSum+pages<=mid:
                    currSum+=pages
                else:
                    currSum=pages
                    student+=1
            return student <= M
        while left<=right:
            mid=(left+right)//2
            # print(isPossible(mid))
            if isPossible(mid):
                # print(hi)
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result
