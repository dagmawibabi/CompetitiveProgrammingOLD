class Solution(object):
    def targetIndices(self, nums, target):
        workingArray = nums;
        workingArray.sort()
        result = []
        while target in workingArray:
            result.append(workingArray.index(target))
            workingArray[workingArray.index(target)] = ""
        return result
