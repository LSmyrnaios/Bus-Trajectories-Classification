import math
import os
import time
from concurrent.futures import ProcessPoolExecutor

from NearestNeighbors.K_arrayList.K_Mins import KMins
from NearestNeighbors.task2A1.DTW import Dtw
from SupportMethods import GetCoordinates, readDatasets, TrainData, GmPlot


def findKnearestNeighborsForTest(testNum, trajectoryTest, K, dtw, maxWarpingWindowPercentage, plotPatterns,
                                 storeMapsDir, makeListOfAllNeighbors, journeyPatternIDs, trainTrajs, trainListSize,
                                 startTime):
    inf_costs_count = 0
    testNum += 1
    print('Checking for ' + K.__str__() + ' nearest-neighbors of test ' + testNum.__str__() + '..')

    # print trajectoryTest # DEBUG!
    min_cost = 1000
    minJourneyPatternId = ''
    min_i = 0
    kMins = KMins(K)

    for i in range(0, trainListSize):  # IDs and Trajectories are of the same size.

        # For sorter tests..
        # if i == 1500:
        #     break

        curPatternID = journeyPatternIDs[i]
        trajectoryTrain = trainTrajs[i]

        cost = dtw._dtw_distance(trajectoryTest, trajectoryTrain)

        if math.isinf(cost):
            # diff = abs(len(trajectoryTrain) - len(trajectoryTest))
            # print 'returned inf while having a diff of: ' + diff.__str__()
            # print 'We have an inf cost in DTW: test:' + testNum.__str__() + ' - trainPatternID: ' + curPatternID
            inf_costs_count += 1
            continue

        kMins.checkMaxCostAndInsert([i, curPatternID, cost])

        # if not makeListOfAllNeighbors and cost <= 25.5:
        #     print testNum.__str__() + '-' + i.__str__() + ') Cost (lessOrEqual to 25.5): ' + cost.__str__()\
        #           + ' from  journeyPatternID: ' + minJourneyPatternId.__str__()

        if cost < min_cost:
            min_cost = cost
            min_i = i
            minJourneyPatternId = curPatternID
            # print(testNum.__str__() + '-' + min_i.__str__() + ') Found new minCost: ' + min_cost.__str__() \
            #      + ' from journeyPatternID: ' + minJourneyPatternId.__str__())

    curElapsedTime = time.time() - startTime

    sorted_nearestNeighbors = sorted(kMins.getArrayList(), key=lambda tup: tup[2])

    if plotPatterns:  # Plot test
        longitudes, latitudes = GetCoordinates.getCoordinates(trajectoryTest)
        fileName = "dtw" + testNum.__str__() + "-test-Time(sec)_" + curElapsedTime.__str__() + ".html"
        GmPlot.gmPlot(latitudes, longitudes, os.path.join(storeMapsDir, fileName), zoom=13)

    sorted_nearestNeighbors_forTest = []
    sortedInfo = ''

    # Plot trains
    for i in range(0, len(sorted_nearestNeighbors)):

        sortedInfo += "\ni: " + sorted_nearestNeighbors[i][0].__str__() + ", PatternID: " + sorted_nearestNeighbors[i][
            1].__str__() + ", DTW-cost: " + sorted_nearestNeighbors[i][2].__str__()

        # Make a list with all the neighbours
        if makeListOfAllNeighbors:
            sorted_nearestNeighbors_forTest.append(sorted_nearestNeighbors[i][1])

        if plotPatterns:
            curTrainTrajectory = trainTrajs[sorted_nearestNeighbors[i][0]]
            longitudes, latitudes = GetCoordinates.getCoordinates(curTrainTrajectory)
            fileName = "dtw" + testNum.__str__() \
                       + "-train" + sorted_nearestNeighbors[i][0].__str__() + "-PatternID_" \
                       + sorted_nearestNeighbors[i][1].__str__() + "-DTW_" \
                       + sorted_nearestNeighbors[i][2].__str__() + ".html"
            GmPlot.gmPlot(latitudes, longitudes, os.path.join(storeMapsDir, fileName), zoom=13)

    print('\nTest: ' + testNum.__str__() + ') finished in ' + time.strftime("%H:%M:%S", time.gmtime(curElapsedTime)) \
          + '\nMax warping window percentage: ' + maxWarpingWindowPercentage.__str__() + '\n\'Inf\' costs found in this test: ' + inf_costs_count.__str__() \
          + '\nMin_journeyPatternId: ' + minJourneyPatternId.__str__() + ' Min_i: ' + min_i.__str__() + ' Min_cost: ' + min_cost.__str__() \
          + '\nSorted mins: ' + sortedInfo)

    return sorted_nearestNeighbors_forTest


def findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListOfAllNeighbors, trainSet, testSet):
    print('\nKNN-with-DTW starts..')

    journeyPatternIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    storeMapsDir = ''
    if plotPatterns:
        storeMapsDir = os.path.join('..', '..', 'Resources', 'maps', 'task2A1')
        if not os.path.isdir(storeMapsDir):
            os.makedirs(storeMapsDir)

    start_time = time.time()
    dtw = Dtw(n_neighbors=K, max_warping_window_percentage=maxWarpingWindowPercentage)
    sorted_nearestNeighbors_forAllTests = []

    futureResults = []
    with ProcessPoolExecutor() as executor:
        futureResults = [
            executor.submit(findKnearestNeighborsForTest, testNum, trajectoryTest, K, dtw, maxWarpingWindowPercentage,
                            plotPatterns, storeMapsDir, makeListOfAllNeighbors, journeyPatternIDs, trainTrajs,
                            trainListSize, start_time) for testNum, trajectoryTest in enumerate(testSet['Trajectory'])]

    if makeListOfAllNeighbors:  # Make a list with all the neighbours for all the tests
        # After all tests have finished, add the results.
        for testNum, future in enumerate(futureResults):
            try:
                result = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (testNum, exc))
            else:
                sorted_nearestNeighbors_forAllTests.append(result)
                # TODO - Fix: "TypeError: object of type 'NoneType' has no len()", inside "NearestNeighbors\task3\GetVotes.py", line: for x in range(len(test)):
                # check: https://docs.python.org/3/library/asyncio-future.html
                # https://docs.python.org/3/library/concurrent.futures.html

    print("\nElapsed time of KNNwithDTW for 'test_set_a1': ",
          time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
    return sorted_nearestNeighbors_forAllTests


if __name__ == '__main__':
    dynamic_datasets_path = os.path.join('..', '..')
    dataSets = readDatasets.read_dataset(True, True, False, dynamic_datasets_path)

    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    K = 5
    plotPatterns = True
    makeListOfAllNeighbors = False
    maxWarpingWindowPercentage = 0.11
    findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListOfAllNeighbors, trainSet, testSetA1)

    exit()
