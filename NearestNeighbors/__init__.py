from NearestNeighbors import task2A1, task2A2
from SupportMethods import readDatasets


def runA1andA2():

    dataSets = readDatasets.read_dataset(True, True, False)

    trainSet = dataSets[0]
    testSet = dataSets[1]

    K = 5
    maxWarpingWindowPercentage = 0.11
    makeListOfAllNeighbors = False
    plotPatterns = True

    task2A1.findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListOfAllNeighbors, trainSet, testSet)

    # This doesn't take any dataSets as parameters.. i gets the in its own
    task2A2.runLCSS(K) #, False)


if __name__ == '__main__':
    runA1andA2()
