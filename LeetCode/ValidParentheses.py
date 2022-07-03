class Solution(object):
    def isValid(self, s):
        workingArray = []
        isValidB = True
        if len(s) % 2 == 0:        
            for i in s:
                workingArray.append(i)
            for i in range(0, len(workingArray), 2):
                j = i + 1
                currentTwo = (workingArray[i] + workingArray[j])
                if currentTwo == "()" or currentTwo == "[]" or currentTwo == "{}":
                    isValidB = True;
                else:
                    isValidB = False
        else:
            isValidB = False
        return isValidB
