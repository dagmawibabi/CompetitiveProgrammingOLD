class Solution(object):
    def maxOperations(self, nums, k):
        workingArray = nums
        targetSum = k;
        sums = []
        for i in workingArray:
            for j in workingArray:
                if i + j == targetSum:
                    sums.append([i, j])
                    workingArray.remove(i)
        return len(sums)
