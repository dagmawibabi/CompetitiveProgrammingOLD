class Solution(object):
    def fib(self, n):
        prev = 0;
        current = 1;
        for i in range(n):
            prev, current = current, prev + current,
        return prev
        