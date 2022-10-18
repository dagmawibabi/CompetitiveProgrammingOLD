class Solution(object):
    def chalkReplacer(self, chalk, k):
        k %= sum(chalk)
        for i, x in enumerate(chalk):
            if k < x:
                return i
            k -= x
        return -1
        