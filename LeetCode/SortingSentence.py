class Solution(object):
    def sortSentence(self, s):
        unsorted = []
        originalSentence = []
        jumbledWords = s.split(" ");
        for i in jumbledWords:
            unsorted.append(i[-1:])
        unsorted.sort()
        for i in unsorted:
            for j in jumbledWords:
                if j[-1:] == i:
                    originalSentence.append(j[:-1])
        return " ".join(originalSentence)