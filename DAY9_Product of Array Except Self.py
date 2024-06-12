class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]
        for i in range(len(nums)-1):
            output.append(output[i]*nums[i])
        for j in range(len(nums)-2,-1,-1):
            output[j]=output[j]*nums[j+1]
            nums[j]=nums[j]*nums[j+1]
        return output

        

            
