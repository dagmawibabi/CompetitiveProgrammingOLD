# class Solution(object):
def lengthOfLongestSubstring(self, s):
    workingList = [];
    longest = [];
    for i in s:
        if i not in workingList:
            workingList.append(i);
        else:
            if len(workingList) > len(longest):
                longest = workingList;
            workingList = []; 
    return len(longest);
            
        