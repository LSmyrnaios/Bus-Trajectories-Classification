import operator
from NearestNeighbors.task2A1 import findKnearestNeighbors
from SupportMethods import readDatasets
from SupportMethods.GetVotes import getVotes
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

    # accuracies = []
    # num_folds = 10
    # subset_size = len(trainSet)/num_folds
    #
    # for i in range(num_folds):
    #
    #     testing_this_round = trainSet[i*subset_size:][:subset_size]
    #     training1 = trainSet[0:][:subset_size * i]
    #     training2 = trainSet[(i+1)*subset_size:][:subset_size*(10-i-1)]
    #
    #     training_this_round = training1 + training2#np.concatenate((training1, training2), axis=0)
    #
    #     #print training2['journeyPatternId']
    #
    #     neighborsTestsLists = findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListsOfNeighborsForAllTests,
    #                                                 training2, testing_this_round)
    #
    #     testData = getVotes(neighborsTestsLists)
    #
    #     print(testData)
    #
    #     correct = 0
    #     i=0
    #     for row in trainSet['journeyPatternId']:
    #         if(i==100):break
    #         try:
    #             print "Predicted: ", testData[i][1], ' - ', "Actual: ", row
    #             if(testData[i][1] is row):
    #                 correct += 1
    #         except: #IndexError:
    #             break
    #         i+=1
    #
    #
    #     print 'Correct predictions: ', correct
    #     print 'Accuacy: ', float(correct)/100


if __name__ == '__main__':
    K = 5
    runClassification(K)
