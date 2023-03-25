import os

from NearestNeighbors.task2A1 import findKnearestNeighbors
from NearestNeighbors.task3.GetVotes import getVotes
from NearestNeighbors.task3.crossValidation import crossValidation
from SupportMethods import readDatasets
from SupportMethods.writePredictionsToCsv import write_predictions_to_csv


def runClassification(K, trainSet, testSet, maxWarpingWindowPercentage):
    print('Start KNN Classification..')

    makeListsOfNeighborsForAllTests = True
    plotPatterns = False  # We just want the KNN, not the html-maps.

    ### Run KNN for test_a2

    neighborsTestsLists = findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns,
                                                makeListsOfNeighborsForAllTests, trainSet, testSet)
    if len(neighborsTestsLists) == 0:
        print("No \"neighborsTestsLists\" could be retrieved!")
        return

    testData = getVotes(neighborsTestsLists)

    write_predictions_to_csv(testData)


if __name__ == '__main__':
    K = 5
    dynamic_datasets_path = os.path.join('..', '..')

    dataSets = readDatasets.read_dataset(True, False, True, dynamic_datasets_path)
    trainSet = dataSets[0]
    testSet = dataSets[1]

    maxWarpingWindowPercentage = 0.33  # For testSet_a2, we need a bigger window to get the right patternIDs.

    runClassification(K, trainSet, testSet, maxWarpingWindowPercentage)

    ### Run 10-fold cross-validation.
    crossValidation(trainSet, K, maxWarpingWindowPercentage, num_folds=10)

    exit()
