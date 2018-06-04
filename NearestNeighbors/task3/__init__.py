from NearestNeighbors.task2A1 import findKnearestNeighbors
from NearestNeighbors.task3.crossValidation import crossValidation
from SupportMethods import readDatasets
from NearestNeighbors.task3.GetVotes import getVotes
from SupportMethods.writePredictionsToCsv import write_predictions_to_csv


def runClassification(K):

    print 'Start KNN Classification..'

    dataSets = readDatasets.read_dataset(True, False, True)
    trainSet = dataSets[0]
    testSet = dataSets[1]

    makeListsOfNeighborsForAllTests = True
    plotPatterns = False    # We just want the KNN, not the html-maps.

    maxWarpingWindowPercentage = 0.33  # For testSet_a2, we need a bigger window to get the right patternIDs.


    # Run KNN for test_a2

    neighborsTestsLists = findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListsOfNeighborsForAllTests,
                                                trainSet, testSet)

    testData = getVotes(neighborsTestsLists)

    write_predictions_to_csv(testData)

    # Run cross-validation.
    crossValidation(K, maxWarpingWindowPercentage, trainSet, num_folds=10)


if __name__ == '__main__':
    K = 5
    runClassification(K)
