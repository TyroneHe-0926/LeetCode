class ToolBox:
    def seperate_string_number(self, string):
        """Split numbers, non alphas, and alphas in a string"""
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