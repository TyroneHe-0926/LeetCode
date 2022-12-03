class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)//2
        a,b = s[:l], s[l:]
        va, vb = 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for c in a:
            c = c.lower()
            if c in vowels: va += 1
        
        for c in b:
            c = c.lower()
            if c.lower() in vowels: vb += 1

        return va == vb


s = Solution()
print(s.halvesAreAlike("AbCdEfGh"))