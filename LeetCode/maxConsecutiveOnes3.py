class Solution(object):
    def longestOnes(self, nums, k):
        ans = 0
        l = 0
        for r, a in enumerate(nums):
          if a == 0:
            k -= 1
          while k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
          ans = max(ans, r - l + 1)

        return ans