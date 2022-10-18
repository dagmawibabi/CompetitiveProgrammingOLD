class Solution(object):
    def findTheWinner(self, n, k):
        def f(idx, n, k):
            if n == 1:
                return 0
            return (k+f((idx+k)%n, n-1, k))%n
        
        return f(0, n, k)+1