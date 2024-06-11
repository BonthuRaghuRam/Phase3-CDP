def findPivotIndex(nums,left,right):
    pivot=nums[right]
    position=left
    for index in range(left,right):
        if nums[index]<pivot:
            nums[index],nums[position]=nums[position],nums[index]
            position+=1
    nums[right],nums[position]=nums[position],nums[right]
    return position
    
def sortNums(nums,left,right):
    if left>=right:
        return 
    pivotIndex=findPivotIndex(nums,left,right)
    sortNums(nums,left,pivotIndex-1)
    sortNums(nums,pivotIndex+1,right)
def performQuickSort(nums):
    n=len(nums)
    sortNums(nums,0,n-1)
nums=[12,50,33,1,45,4,6,20]
performQuickSort(nums)
print(nums)
