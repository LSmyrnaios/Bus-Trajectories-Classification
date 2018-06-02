import operator

from NearestNeighbors.ass2A1 import findKnearestNeighbors
from SupportMethods import readDatasets
from SupportMethods.writePredictionsToCsv import write_predictions_to_csv


def runClassification(K):

    print 'I am happy to help you classify!'


    dataSets = readDatasets.read_dataset(True, False, True)
    trainSet = dataSets[0]
    testSet = dataSets[1]


    makeListOfAllNeighbors = True

    neighborsTestList = findKnearestNeighbors(K, makeListOfAllNeighbors, trainSet, testSet)

    neighborsTestList[0].append("1500")

    # patterns = ['15466', '15466', '15466', '58984', '58984', '96548', '58984', '58984']

    testNum = 0
    testData = []
    for test in neighborsTestList:

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


    write_predictions_to_csv(testData)


    # 1/10 train
    # gia ka8e train
    # Split train_dataset into 0.7% train and 0.3% test.
    # train_x, test_x, train_y, test_y = train_test_split(train_data[headers[2:4]], train_data[headers[-1]], train_size=0.7, test_size=0.3)



if __name__ == '__main__':

    dataSets = readDatasets.read_dataset(True, True, False)

    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    K = 5
    runClassification(K)
