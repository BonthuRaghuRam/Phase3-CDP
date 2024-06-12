class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in ans:
                ans[sorted_word]=[]
            ans[sorted_word].append(word)
        return list(ans.values())

  # Appraoch II
  class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        baseValue = ord('a')
        store = {}

        for word in strs:
            token = ""
            frequency = [0] * 26
            for ch in word:
                currValue = ord(ch) 
                index = currValue - baseValue
                frequency[index] += 1
            for value in frequency:
                token += str(value)
                token += "#"
            if token in store:
                store[token].append(word)
            else:
                store[token] = [word]

        for key in store.keys():
            result.append(store[key])

        return result
