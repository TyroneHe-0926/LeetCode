from collections import defaultdict
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        codemap, freqmap = defaultdict(str), defaultdict(int)

        for mc, alpha in zip(morse, alphabet): codemap[alpha] = mc

        for word in words:
            msg = ""
            for c in word: msg += codemap[c]
            freqmap[msg] += 1
        
        return len(freqmap)

        

soln = Solution()
words = ["gin","zen","gig","msg"]
soln.uniqueMorseRepresentations(words=words)
words = ['a']
soln.uniqueMorseRepresentations(words=words)