# The read4 API is already defined for you.
from typing import List

def read4(buf4: List[str]) -> int:
    pass

class Solution:
    local_buf4 = [""]*4
    local_read = 4
    local_max = 4
    def read(self, buf: List[str], n: int) -> int:
        read_count = 0
        while read_count < n:
            if self.local_read < self.local_max:
                buf[read_count] = self.local_buf4[self.local_read]
                read_count += 1
                self.local_read += 1
                continue
        
            cur_read = read4(self.local_buf4)
            if cur_read == 0:
                break
                
            self.local_max = cur_read
            self.local_read = 0
        return read_count