class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        subStr = []

        for i in s:
            if i != ')':
                stack.append(i)
            else:
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        stack.extend(subStr)
                        subStr = []
                        break
                    subStr += stack.pop()
                
        return ''.join(stack)
        