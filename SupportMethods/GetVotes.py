

def getVotes(neighborsTestsLists):

    testNum = 0
    testData = []
    for test in neighborsTestsLists:
        testNum += 1
        classVotes = {}
        for x in range(len(test)):
            response = test[x]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1

        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        print sortedVotes

        testData.append((testNum, sortedVotes[0][0]))

    return testData