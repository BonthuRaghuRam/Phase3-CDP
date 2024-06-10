class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1=len(word1)
        n2=len(word2)
        n=n1+n2
        cache=[[-1]*n2 for i in range(n1)]
        # Memoization Approach 
        def recursiveApproach(index1,index2):
            if index1==n1 or index2==n2:
                return 0
            elif cache[index1][index2] != -1:
                return cache[index1][index2]
            elif word1[index1]==word2[index2]:
                cache[index1][index2] = 1+recursiveApproach(index1+1,index2+1)
                return cache[index1][index2]
            choice1=recursiveApproach(index1+1,index2)
            choice2=recursiveApproach(index1,index2+1)
            cache[index1][index2]=max(choice1,choice2)
            return cache[index1][index2]
        return n-2*recursiveApproach(0,0)
        def tabulationApproach():
            cache=[[0]*(n2+1) for i in range(n1+1)]
            for index1 in range(n1-1,-1,-1):
                for index2 in range(n2-1,-1,-1):
                    if word1[index1] == word2[index2]:
                        cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
                    else:
                        choice1 = cache[index1 + 1][index2]
                        choice2 = cache[index1][index2 + 1]
                        cache[index1][index2] = max(choice1, choice2)
 
            return cache[0][0]
        return n-2*tabulationApproach()


        
