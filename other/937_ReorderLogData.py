from typing import List
from collections import defaultdict

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = defaultdict(list), []
        for log in logs:
            log_arr = log.split(" ")
            header, content = log_arr[0], log_arr[1:]
            if "".join(content).isdigit(): 
                digit_logs.append(f"{header} {' '.join(content)}")
            else:
                letter_logs[" ".join(content)].append(header)
                letter_logs[" ".join(content)].sort()
                
        letter_logs = dict(sorted(letter_logs.items(), key=lambda x: x[0]))

        return [f"{header} {content}" for content in letter_logs for header in letter_logs[content]] + digit_logs

solution = Solution()
print(solution.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(solution.reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(solution.reorderLogFiles(logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]))