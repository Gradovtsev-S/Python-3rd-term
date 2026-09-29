class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c  in '([{':
                q.append(c)
            elif c in ')]}':
                if not q or q[-1] != d[c]:
                    return False
                q.pop()
        return not q
