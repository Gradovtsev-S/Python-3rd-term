class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        r = 0
        for i in range(len(s) - 1):
            if dict[s[i]] < dict[s[i + 1]]:
                r -= dict[s[i]]
            else :
                r += dict[s[i]]
        r += dict[s[-1]]
        return r