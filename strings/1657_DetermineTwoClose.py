from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1cmap, w2cmap = defaultdict(int), defaultdict(int)
        w1fmap, w2fmap = defaultdict(int), defaultdict(int)

        #construct char to freq map
        for c in word1: w1cmap[c] += 1
        for c in word2: w2cmap[c] += 1

        #check if word2 has every char in word1
        #construct freq to numChar map
        for k, v in w1cmap.items():
            if k not in w2cmap: return False
            w1fmap[v] += 1
        
        for k,v in w2cmap.items():
            w2fmap[v] += 1
        
        #check if the same frequencies have the same amount of letter
        for k,v in w1fmap.items():
            if w2fmap[k] != v: return False

        return True
        

s = Solution()
word1 = "abc" 
word2 = "bca"
print(s.closeStrings(word1, word2))
word1 = "a"
word2 = "aa"
print(s.closeStrings(word1, word2))
word1 = "cabbba"
word2 = "abbccc"
print(s.closeStrings(word1, word2))