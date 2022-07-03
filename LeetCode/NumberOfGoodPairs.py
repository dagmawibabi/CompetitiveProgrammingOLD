class Solution(object):
    def numIdenticalPairs(self, nums):
        goodPairs = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        goodPairs += 1
        return goodPairs
        