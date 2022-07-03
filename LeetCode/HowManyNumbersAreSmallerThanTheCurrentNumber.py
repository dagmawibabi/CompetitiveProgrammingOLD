class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        workingArray = nums;
        result = []
        for i in workingArray:
            numsSmaller = 0;
            for j in workingArray:
                if i != j:
                    if i > j:
                        numsSmaller += 1
            result.append(numsSmaller)
        return result