class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        n=len(beginWord)
        Q=[[beginWord,1]]
        visited=set()
        visited.add(beginWord)
        while Q:
            curr=Q.pop(0)
            if curr[0] == endWord:
                return curr[1]
            word=list(curr[0])
            for index in range(n):
                oldchar=word[index]
                for i in range(97,123):
                    letter=chr(i)
                    word[index]=letter
                    currWord="".join(word)
                    if currWord in wordList and currWord not in visited:
                        visited.add(currWord)
                        Q.append([currWord,curr[1]+1])
                word[index] = oldchar
        return 0
            
