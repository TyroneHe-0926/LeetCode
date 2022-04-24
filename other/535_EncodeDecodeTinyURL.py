import hashlib
from collections import defaultdict

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class Codec:
    urlmap = defaultdict(str)
    def encode(self, longUrl: str) -> str:
        header = longUrl.split('//')[0] + '//'
        longUrl = longUrl.split(header)[1]
        encoded = md5(longUrl)[-8:]
        self.urlmap[encoded] = longUrl
        return header + encoded

    def decode(self, shortUrl: str) -> str:
        header = shortUrl.split('//')[0] + '//'
        encoded = shortUrl.split(header)[1]
        decoded = self.urlmap[encoded]
        return header + decoded

        
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
print(codec.encode(url))
print(codec.decode(url))
print(md5(url))