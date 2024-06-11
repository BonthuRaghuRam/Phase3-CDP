def performSelectionSort(nums,n):
    if n==1:
        return n
    maxValueIndex=n-1
    for i in range(n-1):
        if nums[i]>nums[maxValueIndex]:
            maxValueIndex=i
    if maxValueIndex!=n-1:
        nums[n-1],nums[maxValueIndex] = nums[maxValueIndex],nums[n-1]
    performSelectionSort(nums,n-1)
nums=[9,1,8,7,6,3,5]
performSelectionSort(nums,len(nums))
print(nums)
