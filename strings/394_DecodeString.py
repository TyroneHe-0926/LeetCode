class Solution:
    def decodeString(self, s: str) -> str:
        s = self.seperate_string_number(s)
        digit_stack, word_stack, curstr = [], [], ""
        for index, c in enumerate(s):
            if c == '[':
                digit_stack.append(int(s[index-1]))
                word_stack.append(curstr)
                curstr = ""
            elif c == ']':
                word = word_stack.pop()
                digit = digit_stack.pop()
                curstr = word + digit*curstr
            elif c.isalpha(): curstr += c
        
        return curstr

    def seperate_string_number(self, string):
        previous_character = string[0]
        groups = []
        newword = string[0]
        for x, i in enumerate(string[1:]):
            if i.isalpha() and previous_character.isalpha():
                newword += i
            elif i.isnumeric() and previous_character.isnumeric():
                newword += i
            else:
                groups.append(newword)
                newword = i

            previous_character = i

            if x == len(string) - 2:
                groups.append(newword)
                newword = ''
        return groups if groups else [string]

solution = Solution()
# print(solution.decodeString("3[a2[c]]"))
print(solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
# print(solution.decodeString("4[2[jk]el]"))
print(solution.decodeString("2[abc]3[cd]ef"))
# print(solution.decodeString("3[a2[b8[c]]]"))
# print(solution.decodeString("31[a]28[bc]"))
# print(solution.decodeString("a"))