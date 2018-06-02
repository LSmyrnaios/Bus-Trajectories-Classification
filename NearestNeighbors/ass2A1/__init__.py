import time
from NearestNeighbors.ass2A1.DTW import Dtw
from SupportMethods import GetCoordinates, readDatasets, TrainData
from DataVisualisation import GmPlot


def findKnearestNeighbors(K, makeListOfAllNeighbors, trainSet, testSet):

    i=0
    min_cost = 0
    min_train_trajectory = []
    minJourneyId = 0
    min_i = 0

    dtw = Dtw()
    #dtw.fit(trainSet, 1)
    #dtw.predict(testSet)
    #dtw._dtw_distance(trainSet['Trajectory'][1], testSet[1])

    journeyPatternIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    start_time = time.time()
    lastTime = start_time   # For in-the-middle elapsed-time.

    sorted_nearestNeighbors_foralltests = []

    testNum = 0
    for trajectoryTest in testSet['Trajectory']:

        testNum += 1
        if testNum < 2:
            continue
        if testNum == 3:
            break

        nearestNeighbors = []
        sorted_nearestNeighbors = []

        print '\nChecking for ' + K.__str__() + ' nearest-neighbors of test ' + testNum.__str__()

        # print trajectoryTest # DEBUG!

        for i in range(0, trainListSize):  # IDs and Trajectories are of the same size.

            # print journeyPatternIDs[i] # DEBUG!

            trajectoryTrain = trainTrajs[i]
            # print trajectoryTrain

            cost = dtw._dtw_distance(trajectoryTest, trajectoryTrain)
            nearestNeighbors.append((i, journeyPatternIDs[min_i], cost))
            # print i.__str__() + ') Cost: ' + cost.__str__()
            if i == 0:
                min_cost = cost
                min_train_trajectory = trajectoryTrain
            elif cost < min_cost:
                min_cost = cost
                min_train_trajectory = trajectoryTrain
                min_i = i
                minJourneyId = journeyPatternIDs[min_i]
                print testNum.__str__() + '-' + min_i.__str__() + ') Found new minCost: ' + min_cost.__str__()\
                      + ' from  journeyPatternID: ' + minJourneyId.__str__()

            if i == 360:
                break

            #print 'long: ' + trajectoryTest[1][1].__str__() + ' lat: ' + trajectoryTest[1][2].__str__()
            #print 'long: ' + trajectoryTrain[1][1].__str__() + ' lat: ' + trajectoryTrain[1][2].__str__()

        curTime = time.time()
        curElapsedTime = curTime - lastTime
        lastTime = curTime

        sorted_nearestNeighbors = sorted(nearestNeighbors, key=lambda tup: tup[2])

        print '\nTest: ' + testNum.__str__() + ') finished in ' + time.strftime("%H:%M:%S", time.gmtime(curElapsedTime))\
              + '\nMin_journeyId: ' + minJourneyId.__str__() + ' min_i: ' + min_i.__str__()\
              + ' Min_long: ' + min_train_trajectory[1][1].__str__() + ' Min_lat: ' + min_train_trajectory[1][2].__str__() + ' Min_cost: ' + min_cost.__str__()\
              + '\nSorted mins: '
        for i in range(0, K):
            print  "i: ", sorted_nearestNeighbors[i][0], " PatternID: ", sorted_nearestNeighbors[i][1], " , cost: ", sorted_nearestNeighbors[i][2]

        # Plot test
        longtitutes, latitudes = GetCoordinates.getCoordinates(trajectoryTest)
        GmPlot.gmPlot(latitudes, longtitutes, "../../Resources/maps/task2A1/dtw" + testNum.__str__() + "-test.html")

        sorted_nearestNeighbors_fortest = []

        # Plot trains
        for i in range(0, K):
            # Make a list with all the neighbours
            if makeListOfAllNeighbors:
                sorted_nearestNeighbors_fortest.append(sorted_nearestNeighbors[i][1])
            curTrainTrajectory = trainTrajs[sorted_nearestNeighbors[i][0]]
            longtitutes, latitudes = GetCoordinates.getCoordinates(curTrainTrajectory)
            GmPlot.gmPlot(latitudes, longtitutes, "../../Resources/maps/task2A1/dtw" + testNum.__str__()
                          + "-train" + (i+1).__str__() + "_PatternID_" + journeyPatternIDs[i].__str__() + ".html")

        # Make a list with all the neighbours for all the tests
        sorted_nearestNeighbors_foralltests.append(sorted_nearestNeighbors_fortest)


    print "\nElapsed time of KNNwithDTW for 'test_set_a1': ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)), 'mins'

    return sorted_nearestNeighbors_foralltests


if __name__ == '__main__':

    dataSets = readDatasets.read_dataset(True, True, False)

    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    K = 5
    makeListOfAllNeighbors = False
    findKnearestNeighbors(K, makeListOfAllNeighbors, trainSet, testSetA1)
