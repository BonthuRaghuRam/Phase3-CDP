class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        result=0
        store=set()
        left,right=0,0
        while right<n:
            while s[right] in store:
                store.remove(s[left])
                left+=1
            store.add(s[right])
            right+=1
            result=max(result,len(store))
        return result
