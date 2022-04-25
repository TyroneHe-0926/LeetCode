class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        """
        Two things, 
        1. you cant have adjacent abbvs so i kept track of a abbed bool var,
        bascially you cant have 2 trues in a row

        2. No leading zeros. so when i see a digit, it has a follow up, update the i index to i+2,
        so even if its sth like 101, or 10, its fine, as long as its not 010, or any leading 0
        """

        sindex, i, full, abbed = 0, 0, "", False
        while i < len(abbr):
            if not abbr[i].isdigit(): full, sindex, i, abbed = full+abbr[i], sindex+1, i+1, False
            else:
                if i+1 < len(abbr) and abbr[i+1].isdigit():
                    skip = int(abbr[i]+abbr[i+1])
                    if sindex+skip > len(word) or abbr[i] == '0' or abbed: return False
                    full, sindex, i, abbed = full+word[sindex:sindex+skip], sindex+skip, i+2, True
                else: 
                    skip = int(abbr[i])
                    if sindex+skip > len(word) or skip == 0 or abbed: return False
                    full, sindex, i, abbed = full+word[sindex:sindex+skip], sindex+skip, i+1, True
            
        return full == word

s = Solution()
print(s.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n"))
print(s.validWordAbbreviation(word = "aaaaaaaaaaaaaaaaaaa", abbr = "145"))
print(s.validWordAbbreviation(word = "a", abbr = "01"))
print(s.validWordAbbreviation(word = "a", abbr = "1"))
print(s.validWordAbbreviation(word = "apple", abbr = "a2e"))
print(s.validWordAbbreviation(word = "apple", abbr = "a3e"))