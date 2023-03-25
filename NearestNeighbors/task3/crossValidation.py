import os

from NearestNeighbors.task2A1 import findKnearestNeighbors
from NearestNeighbors.task3.GetVotes import getVotes
from SupportMethods import readDatasets


def crossValidation(trainSet, K, maxWarpingWindowPercentage, num_folds=10):
    accuracies = []
    subset_size = int(len(trainSet) / num_folds)
    accuracy = 0

    for i in range(num_folds):

        print("cross-validation: " + (i + 1).__str__())

        testing_this_round = trainSet[i * subset_size:][:subset_size]  # TODO - This is huge!
        training1 = trainSet[0:][:subset_size * i]
        training2 = trainSet[(i + 1) * subset_size:][:subset_size * (10 - i - 1)]

        training_this_round = training1 + training2  # np.concatenate((training1, training2), axis=0)

        # print training2['journeyPatternId']

        makeListsOfNeighborsForAllTests = True
        plotPatterns = False  # We just want the KNN, not the html-maps.

        neighborsTestsLists = findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns,
                                                    makeListsOfNeighborsForAllTests,
                                                    training2, testing_this_round)

        testData = getVotes(neighborsTestsLists)

        print(testData)

        correct = 0
        for j, row in enumerate(trainSet['journeyPatternId']):
            if j == 100:
                break
            try:
                print("Predicted: ", testData[i][1], ' - ', "Actual: ", row)
                if testData[i][1] is row:
                    correct += 1
            except IndexError:
                break

        print('Correct predictions: ', correct)
        accuracy = float(correct) / 100
        print('Accuracy: ', accuracy)

    return accuracy


if __name__ == '__main__':
    dynamic_datasets_path = os.path.join('..', '..')
    dataSets = readDatasets.read_dataset(True, False, False, dynamic_datasets_path)

    trainSet = dataSets[0]
    crossValidation(trainSet, K=5, maxWarpingWindowPercentage=0.33, num_folds=10)
    exit()
