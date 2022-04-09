class Solution:
    def isNumber(self, s: str) -> bool:
        if 'inf' in s.lower():
            return False
        try:
            a = int(s)
            return True
        except ValueError:
            res = False
        try:
            a = float(s)
            return True
        except ValueError:
            res = False
        return res


class Solution(object):
    """LC DFA"""
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        state = [{}, 
                {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
                {'digit':3, '.':4},
                {'digit':3, '.':5, 'e':6, 'blank':9},
                {'digit':5},
                {'digit':5, 'e':6, 'blank':9},
                {'sign':7, 'digit':8},
                {'digit':8},
                {'digit':8, 'blank':9},
                {'blank':9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True

class Solution:
    """LC BF"""
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot =  False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        
        return seen_digit