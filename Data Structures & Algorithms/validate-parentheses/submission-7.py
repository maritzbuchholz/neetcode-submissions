class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False