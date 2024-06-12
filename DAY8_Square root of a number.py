class Solution:
    def floorSqrt(self, x): 
        left=1
        right=x
        result=1
        while left<=right:
            mid=(left+right)//2
            if mid*mid<=x:
                result=mid
                left=mid+1
            else:
                right=mid-1
        return result
