class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def firstOccurence(left,right):
            result=-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]==target:
                    result=mid
                    right=mid-1
                elif arr[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return result
        def lastOccurence(left,right):
            result=-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]==target:
                    result=mid
                    left=mid+1
                elif arr[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return result
        a=firstOccurence(0,len(arr)-1)
        b=lastOccurence(0,len(arr)-1)
        return [a,b]

        
