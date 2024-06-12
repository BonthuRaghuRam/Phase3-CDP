class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        box={}
        n=len(nums)
        for index in range(n-1,-1,-1):
            otherElement=target-nums[index]
            if otherElement in box:
                return [index,box[otherElement]]
            box[nums[index]]=index
        return []
