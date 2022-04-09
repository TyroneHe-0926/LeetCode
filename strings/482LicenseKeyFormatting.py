class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        str_len = len(s)
        str_arr = []
        extras = str_len % k
        if extras != 0:
            str_arr.append(s[:extras])
            s = s[extras:]
        
        for i in range(0, str_len, k):
            substr = s[i:i+k]
            if substr:
                str_arr.append(substr)
        
        return ("-".join(str_arr)).upper()

if __name__ == "__main__":
    solution = Solution()
    s = "2-4A0r7-4k"
    k = 3
    print(solution.licenseKeyFormatting(s, k))
    s = "2"
    k = 1
    print(solution.licenseKeyFormatting(s, k))