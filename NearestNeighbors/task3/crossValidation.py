from NearestNeighbors.task2A1 import findKnearestNeighbors
from SupportMethods import readDatasets
from NearestNeighbors.task3.GetVotes import getVotes


def crossValidation(K, maxWarpingWindowPercentage, trainSet, num_folds=10):

    accuracies = []
    subset_size = len(trainSet)/num_folds

    for i in range(num_folds):

        testing_this_round = trainSet[i*subset_size:][:subset_size]
        training1 = trainSet[0:][:subset_size * i]
        training2 = trainSet[(i+1)*subset_size:][:subset_size*(10-i-1)]

        training_this_round = training1 + training2#np.concatenate((training1, training2), axis=0)

        #print training2['journeyPatternId']

        neighborsTestsLists = findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListsOfNeighborsForAllTests,
                                                    training2, testing_this_round)

        testData = getVotes(neighborsTestsLists)

        print(testData)

        correct = 0
        i=0
        for row in trainSet['journeyPatternId']:
            if(i==100):break
            try:
                print "Predicted: ", testData[i][1], ' - ', "Actual: ", row
                if(testData[i][1] is row):
                    correct += 1
            except: #IndexError:
                break
            i+=1


        print 'Correct predictions: ', correct
        accuracy = float(correct)/100
        print 'Accuacy: ', accuracy

    return accuracy


if __name__ == '__main__':
    dataSets = readDatasets.read_dataset(True, False, False)
    trainSet = dataSets[0]

    crossValidation(trainSet, K=5, maxWarpingWindowPercentage=0.33, num_folds=10)