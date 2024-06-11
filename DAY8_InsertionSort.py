def insertionSort(nums,n):
    if n==1:
        return 
    insertionSort(nums,n-1)
    curValue=nums[n-1]
    prevIndex=n-2
    while prevIndex>=0:
        if nums[prevIndex]>curValue:
            nums[prevIndex+1]=nums[prevIndex]
        else:
            break
        prevIndex-=1
    nums[prevIndex+1]=curValue
nums=[9,1,8,7,6,3,5]
insertionSort(nums,len(nums))
print(nums)
