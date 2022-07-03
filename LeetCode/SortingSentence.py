def sortSentence(s):
    a = s.split(" ");
    unsorted = []
    originalSentence = []
    for i in a:
        unsorted.append(i[-1:])
    unsorted.sort();
    for i in unsorted:
        for j in a:
            if j[-1:] == i:
                originalSentence.append(j[:-1]);
    properSentence = ""
    for i in originalSentence:
        properSentence += i + " ";
    print(properSentence);
    print(" ".join(originalSentence))
sortSentence("This1 awesome3 is2");
        