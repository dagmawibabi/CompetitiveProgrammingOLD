class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        summ = sum(cardPoints)
        windowSum = sum(cardPoints[:n - k])
        ans = summ - windowSum

        for i in range(k):
          windowSum -= cardPoints[i]
          windowSum += cardPoints[i + n - k]
          ans = max(ans, summ - windowSum)

        return ans
        