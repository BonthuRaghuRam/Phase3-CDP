class TrieNode:
    def __init__(self):
        self.isEnding = False 
        self.store = dict()
class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root
        n=len(word)
        for index in range(n):
            if word[index] not in curr.store:
                curr.store[word[index]]=TrieNode()
            curr=curr.store[word[index]]
        curr.isEnding=True
    
    def search(self, word: str) -> bool:
        curr=self.root
        n=len(word)
        for index in range(n):
            ch=word[index]
            if ch not in curr.store:
                return False
            curr=curr.store[ch]
        return curr.isEnding
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        n=len(prefix)
        for index in range(n):
            ch=prefix[index]
            if ch not in curr.store:
                return False
            curr=curr.store[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
