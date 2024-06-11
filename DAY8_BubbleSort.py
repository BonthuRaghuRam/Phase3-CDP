nums=[9,1,8,7,6,3,5]
print("Before Sorting: ",nums)
def performBubbleSort(nums,n):
    if n==1:
        return
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
    performBubbleSort(nums,n-1)
performBubbleSort(nums,len(nums))
print(nums)
