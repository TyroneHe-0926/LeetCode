class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first = word[0]
        firstCap = first >= 'A' and first <= 'Z'
        allCap, allLower = True, True

        for c in word[1:]:
            if c >= 'a' and c <= 'z': allCap = False
            if c >= 'A' and c <= 'Z': allLower = False

        if firstCap and allLower: return True
        if firstCap and allCap: return True
        if not firstCap and allLower: return True

        return False

s = Solution()
print(s.detectCapitalUse('mL'))