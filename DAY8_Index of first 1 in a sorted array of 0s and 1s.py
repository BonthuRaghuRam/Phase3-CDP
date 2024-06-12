def firstOccurence(left,right):
            result=-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]==1:
                    result=mid
                    right=mid-1
                else:
                    left=mid+1
            return result
        return firstOccurence(0,n-1)
