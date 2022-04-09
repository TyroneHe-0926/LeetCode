class Solution:
    def reformatDate(self, date: str) -> str:
        mmap = {
            "Jan": "01", "Feb": "02", "Mar": "03", 
            "Apr": "04", "May": "05", "Jun": "06", 
            "Jul": "07", "Aug": "08", "Sep": "09", 
            "Oct": "10", "Nov": "11", "Dec": "12"
        }
        d,m,y = date.split(" ")
        d = '0'+d if len(d) == 3 else d
        return f"{y}-{mmap[m]}-{d[0:2]}"

s = Solution()
print(s.reformatDate(date = "20th Oct 2052"))
print(s.reformatDate(date = "26th May 1960"))
print(s.reformatDate(date = "6th Jun 1933"))