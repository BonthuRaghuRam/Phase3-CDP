class Solution:

	def count(self,arr, n, x):
		def firstOccurence(left,right):
            result=-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]==x:
                    result=mid
                    right=mid-1
                elif arr[mid]>x:
                    right=mid-1
                else:
                    left=mid+1
            return result
        def lastOccurence(left,right):
            result=-1
            while left<=right:
                mid=(left+right)//2
                if arr[mid]==x:
                    result=mid
                    left=mid+1
                elif arr[mid]>x:
                    right=mid-1
                else:
                    left=mid+1
            return result
        a=firstOccurence(0,n-1)
        if a==-1:
            return 0
        b=lastOccurence(0,n-1)
        return b-a+1
        
