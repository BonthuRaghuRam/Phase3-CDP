class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        minSum=max(nums)
        maxSum=sum(nums)
        def isPossible(mid):
            cnt=0
            val=k
            for i in nums:
                if i>mid:
                    return False
                if cnt+i>mid:
                    cnt=i
                    val-=1
                    if val==0:
                        return False
                else:
                    cnt+=i
            return True
        left=minSum
        right=maxSum
        result=-1
        while left<=right:
            mid=(left+right)//2
            if isPossible(mid):
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result

        
