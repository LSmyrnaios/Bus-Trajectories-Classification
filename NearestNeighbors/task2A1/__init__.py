import math
import os
import time
from NearestNeighbors.task2A1.DTW import Dtw
from NearestNeighbors.task2A1.K_Mins import KMins
from SupportMethods import GetCoordinates, readDatasets, TrainData
from DataVisualisation import GmPlot


def findKnearestNeighbors(K, plotPatterns, makeListOfAllNeighbors, trainSet, testSet):

    journeyPatternIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    storeMapsDir = "../../Resources/maps/task2A1"
    if not os.path.isdir(storeMapsDir):
        os.makedirs(storeMapsDir)

    max_warping = 0.11
    dtw = Dtw(max_warping_window_percentage=max_warping)
    kMins = KMins(K)

    sorted_nearestNeighbors_forAllTests = []
    inf_costs_count = 0
    testNum = 0

    start_time = time.time()
    lastTime = start_time   # For in-the-middle elapsed-time.

    for trajectoryTest in testSet['Trajectory']:

        inf_costs_count = 0

        testNum += 1
        # if testNum != 5:
        #     continue
        # if testNum <= 4:
        #     continue
        # if testNum == 3:
        #     print 'InfCount: ' + inf_costs_count.__str__()
        #     break

        print '\nChecking for ' + K.__str__() + ' nearest-neighbors of test ' + testNum.__str__() + '..'

        # print trajectoryTest # DEBUG!
        min_cost = 1000
        minJourneyPatternId = ''
        min_i = 0

        for i in range(0, trainListSize):  # IDs and Trajectories are of the same size.

            # if i == 1500:
            #     break

            trajectoryTrain = trainTrajs[i]
            curPatternID = journeyPatternIDs[i]

            cost = dtw._dtw_distance(trajectoryTest, trajectoryTrain)

            if math.isinf(cost):
                # diff = abs(len(trajectoryTrain) - len(trajectoryTest))
                # print 'returned inf while having a diff of: ' + diff.__str__()
                #print 'We have an inf cost in DTW: test:' + testNum.__str__() + ' - trainPatternID: ' + curPatternID
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
                print testNum.__str__() + '-' + min_i.__str__() + ') Found new minCost: ' + min_cost.__str__()\
                      + ' from  journeyPatternID: ' + minJourneyPatternId.__str__()

        curTime = time.time()
        curElapsedTime = curTime - lastTime
        lastTime = curTime

        sorted_nearestNeighbors = sorted(kMins.getArrayList(), key=lambda tup: tup[2])
        kMins.resetArrayList()  # Reset arrayList before going to the next testSet.

        print '\nTest: ' + testNum.__str__() + ') finished in ' + time.strftime("%H:%M:%S", time.gmtime(curElapsedTime))\
            + '\nMax warping window percentage: ' + max_warping.__str__() + '\n\'Inf\' costs found in this test: ' + inf_costs_count.__str__() \
            + '\nMin_journeyPatternId: ' + minJourneyPatternId.__str__() + ' Min_i: ' + min_i.__str__() + ' Min_cost: ' + min_cost.__str__() \
            + '\nSorted mins: '
        for i in range(0, K):
            print "i: ", sorted_nearestNeighbors[i][0], " PatternID: ", sorted_nearestNeighbors[i][1], " , cost: ", sorted_nearestNeighbors[i][2]

        if plotPatterns:
            # Plot test
            longtitutes, latitudes = GetCoordinates.getCoordinates(trajectoryTest)
            GmPlot.gmPlot(latitudes, longtitutes, storeMapsDir + "/dtw" + testNum.__str__() + "-test.html")

        if plotPatterns or makeListOfAllNeighbors:
            sorted_nearestNeighbors_fortest = []

            # Plot trains
            for i in range(0, K):
                # Make a list with all the neighbours
                if makeListOfAllNeighbors:
                    sorted_nearestNeighbors_fortest.append(sorted_nearestNeighbors[i][1])
                if plotPatterns:
                    curTrainTrajectory = trainTrajs[sorted_nearestNeighbors[i][0]]
                    longtitutes, latitudes = GetCoordinates.getCoordinates(curTrainTrajectory)
                    GmPlot.gmPlot(latitudes, longtitutes, storeMapsDir + "/dtw" + testNum.__str__()
                                  + "-train" + sorted_nearestNeighbors[i][0].__str__() + "_PatternID_" + journeyPatternIDs[i].__str__() + ".html")

        if makeListOfAllNeighbors:
            # Make a list with all the neighbours for all the tests
            sorted_nearestNeighbors_forAllTests.append(sorted_nearestNeighbors_fortest)


    print "\nElapsed time of KNNwithDTW for 'test_set_a1': ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))

    return sorted_nearestNeighbors_forAllTests


if __name__ == '__main__':

    dataSets = readDatasets.read_dataset(True, True, False)

    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    K = 5
    plotPatterns = True
    makeListOfAllNeighbors = False
    findKnearestNeighbors(K, plotPatterns, makeListOfAllNeighbors, trainSet, testSetA1)
