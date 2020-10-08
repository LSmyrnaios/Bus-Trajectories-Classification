from NearestNeighbors import task2A1, task2A2
from SupportMethods import readDatasets


def runA1andA2(K, dynamic_datasets_path):
    dataSets = readDatasets.read_dataset(True, True, False, dynamic_datasets_path)

    trainSet = dataSets[0]
    testSet = dataSets[1]

    maxWarpingWindowPercentage = 0.11
    makeListOfAllNeighbors = False
    plotPatterns = True

    task2A1.findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListOfAllNeighbors, trainSet, testSet)

    # This doesn't take any dataSets as parameters.. it gets them on its own
    task2A2.runLCSS(K, dynamic_datasets_path)


if __name__ == '__main__':
    K = 5
    dynamic_datasets_path = '../'
    runA1andA2(K, dynamic_datasets_path)
    exit()

