class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        result=[]
        index1=0
        while index1<n:
            index2=index1+1
            while index2<n:
                remaining=target-(nums[index1]+nums[index2])
                j=index2+1
                k=n-1
                while j<k:
                    if nums[j]+nums[k]==remaining:
                        result.append([nums[index1],nums[index2],nums[j],nums[k]])
                        j+=1
                        while j<n and nums[j]==nums[j-1]:
                            j+=1
                        k-=1
                        while k<=0 and nums[k]==nums[k+1]:
                            k-=1
                    elif nums[j]+nums[k]>remaining:
                        k-=1
                    else:
                        j+=1
                index2+=1
                while index2<n and nums[index2]==nums[index2-1]:
                    index2+=1
            index1+=1
            while index1<n and nums[index1]==nums[index1-1]:
                index1+=1
        return result

                        
