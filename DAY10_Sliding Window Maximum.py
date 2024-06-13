class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        result=[]
        store=[]
        for i in range(k):
            while store and nums[store[-1]]<=nums[i]:
                store.pop()
            store.append(i)
        result.append(nums[store[0]])
        left,right=0,k
        while right<n:
            if store and store[0]==left:
                store.pop(0)
            while store and nums[store[-1]]<=nums[right]:
                store.pop()
            store.append(right)
            result.append(nums[store[0]])
            left+=1
            right+=1
        return result

        
        
