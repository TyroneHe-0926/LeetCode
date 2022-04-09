class RabinKarp:
    d = 256 #number of chars in extended ascii
    def find(self, src: str, target: str):
        if not src:
            return 0
        if not target:
            return -1
        
        slen, plen = len(src), len(target)
        phash, shash = 0, 0
        h, q = 1, 101
    
        # The value of h would be "pow(d, slen-1)%q"
        for i in range(plen-1):
            h = (h*self.d)%q
    
        # Calculate the hash value of pattern and first window
        # of text
        for i in range(plen):
            phash = (self.d*phash + ord(target[i]))%q
            shash = (self.d*shash + ord(src[i]))%q
    
        # Slide the pattern over text one by one
        for i in range(slen-plen+1):
            # Check the hash values of current window of text and
            # pattern if the hash values match then only check
            # for characters one by one
            if phash==shash:
                # Check for characters one by one
                if src[i:i+plen] == target: print ("Pattern found at index " + str(i))
            # Calculate hash value for next window of text: Remove
            # leading digit, add trailing digit
            if i < slen-plen:
                # We might get negative values of shash, converting it to
                # positive
                shash = abs((self.d*(shash-ord(src[i])*h) + ord(src[i+plen]))%q)
    
solution = RabinKarp()
solution.find(src = "GEEKS FOR GEEKS", target = "GEEK")
solution.find(src = "AAAAAAAA", target = "AAA")