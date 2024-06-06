# one approach
class Solution:
    def subString(self,index,s,tempDict,cache):
        if index==len(s):
            return True
        if cache[index]!=-1:
            if cache[index]==1:
                return True
            return False
        currentWord=""
        for i in range(index,len(s)):
            currentWord+=s[i]
            if currentWord in tempDict:
                res=self.subString(i+1,s,tempDict,cache)
                if res==True:
                    cache[index]==1
                    return True
        cache[index]=0
        return False
    def wordBreak(self, s, wordDict):
        tempDict=list(set(wordDict))
        cache=[-1]*(len(s))
        return self.subString(0,s,tempDict,cache)

# 2nd approach
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordMap = set(wordDict)
        
        memo = [False] * (len(s) + 1)
        memo[len(s)] = True # you can form a word with no letters
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                if memo[j] and s[i:j] in wordMap:
                    memo[i] = True
        return memo[0]
