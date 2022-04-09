class KMP:
    def find(self, src: str, target: str):
        if not src:
            return 0
        if not target:
            return -1
        lps = self.lps_build(pattern=target)
        self.kmp(s=src, pattern=target, lps=lps)
    
    def lps_build(self, pattern):
        lps, plen, i, j = [0], len(pattern), 1, 0
        while i < plen:
            if pattern[i] == pattern[j]:
                j+=1
                lps.append(j)
                i+=1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps.append(0)
                    i+=1
        return lps

    def kmp(self, s, pattern, lps):
        slen, plen, i, j = len(s), len(pattern), 0, 0
        while i < slen:
            if s[i] == pattern[j]:
                i+=1
                j+=1
            if j == plen:
                print(f"Pattern found at {i-j}")
                j = lps[j-1]
            elif i < slen and s[i] != pattern[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i+=1
        return -1