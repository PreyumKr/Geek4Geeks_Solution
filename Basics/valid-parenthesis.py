'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
# solution

class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack=[]
        l = {'(':')','[':']','{':'}'}
        for i in range(len(s)):
            if s[i] in l:
                stack.append(s[i])
            elif len(stack) == 0 or l[stack.pop()] != s[i]:
                return False
        return True if len(stack) == 0 else False