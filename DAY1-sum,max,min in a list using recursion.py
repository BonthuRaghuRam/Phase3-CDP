# #Sum of elements in a list using recursion
# # Backtraking from Parent to child
# def ptoc(i,nums,n,res):
#     if i == n:
#         print(res)
#         return
#     res+=nums[i]
#     ptoc(i+1,nums,n,res)
# # Dynamic from child to parent
# def s(i,n):
#     if len(n)==0:
#         return 0
#     return n[i]+s(0,n[i+1:])
# # maximum in list by passing parent to child
# def maxi(i,nums,n,maximum):
#     if i==n:
#         print(maximum)
#         return
#     # maximum=max(maximum,nums[i])
#     if maximum<nums[i]:
#         maximum=nums[i]
#     maxi(i+1,nums,n,maximum)
# # passing from child to parent
# def maxim(i,nums):
#     if len(nums)==1:
#         return nums[0]
#     return max(nums[i],maxim(0,nums[i+1:]))
# # Minimum
# # passing from parent to child
# def minimum(i,nums,n,res):
#     if i==n:
#         print(res)
#         return
#     res=min(res,nums[i])
#     minimum(i+1,nums,n,res)
# # passing from child to parent
# def mini(i,nums):
#     if len(nums)==1:
#         return nums[0]
#     return min(nums[0],mini(0,nums[1:]))
#
#
#
#
# nums=[12,34,16,5,6,1,50,99]
# n=len(nums)
# ptoc(0,nums,n,0)
# print(s(0,nums))
# maxi(0,nums,n,0)
# print(maxim(0,nums))
# minimum(0,nums,n,nums[0])
# print(mini(0,nums))

