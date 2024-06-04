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
















# def ctop(i,str,count):
#     if i==len(str):
#         print(count)
#         return
#     vowels="aeiou"
#     if str[i] in vowels:
#         count+=1
#     ctop(i+1,str,count)
#
#
# str="abcdeefuigh"
# ctop(0,str,0)

# def c(str1,i,n):
#     if i==n:
#         return 0
#     nextVowelsCount=c(str1,i+1,n)
#     vowels="aeiou"
#     if str1[i] in vowels:
#         nextVowelsCount+=1
#     return nextVowelsCount
#
#
# str1="abcdeefuigh"
# result=c(str1,0,len(str1))
# print(result)

















# # passing from parent to child
# def f(i,str,vowel,consonant):
#     v="aeiou"
#     if i==len(str):
#         print(vowel)
#         print(consonant)
#         return
#     if str[i] in v:
#         vowel+=str[i]
#     else:
#         consonant+=str[i]
#     f(i+1,str,vowel, consonant)
# # passing from child to parent
def f1(i,str):
    vowel=""
    consonant=""
    v="aeiou"
    if i==len(str):
        return 0
    # print(str[i])
    t=f1(i+1,str)
    if str[i] in v:
        t +=str[i]
        return t
    else:
        consonant+=str[i]
        return consonant
    # if i==0:
    #     print(vowel)
    #     print(consonant)

# # def findVowels(index, word, vowel):
# #     vowel="aeiou"
# #     if index == len(word):
# #         return 0
# #     t = findVowels(index + 1, word, vowel)
# #     if word[index] in vowel:
# #         t += 1
# #     return t
#
#
#
#
str="raghu"
# f(0,str,"","")
f1(0,str)
# # str="raghu"
# # v="aeiou"
# # for i in str:
# #     if i in v:
# #         print(i)

