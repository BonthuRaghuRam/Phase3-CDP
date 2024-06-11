def sortThem(nums,left,mid,right):
    temp=[]
    index1=left
    index2=mid+1
    while index1<=mid and index2<=right:
        if nums[index1]>nums[index2]:
            temp.append(nums[index2])
            index2+=1
        else:
            temp.append(nums[index1])
            index1+=1
    while index1<=mid:
        temp.append(index1)
        index1+=1
    while index2<=right:
        temp.append(index2)
        index2+=1
    position = 0 
    for index in range(left, right + 1):
        nums[index] = temp[position]
        position += 1 

def divide(nums,left,right):
    if left>=right:
        return
    mid=(left+right)//2
    divide(nums,left,mid)
    divide(nums,mid+1,right)
    sortThem(nums,left,mid,right)
def mergeSort(nums):
    n=len(nums)
    divide(nums,0,n-1)
nums=[9,1,8,6,5,3,33,-5]
mergeSort(nums)
print(nums)
