class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            minIndex = i
            for j in range( i +1, len(nums)):
                if nums[minIndex] > nums[j]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums;
