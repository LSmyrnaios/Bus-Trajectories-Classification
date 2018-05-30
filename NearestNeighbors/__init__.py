import time
from KNNwithDTW import KnnDtw
from SupportMethods import GmPlot, GetTrajectorySets, readDatasets, TrainData


def findKearestNeighbors():

    # Combine code and find nearest neighbors!

    dataSets = readDatasets.read_dataset(True, True, False)

    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    i=0
    min_cost = 0
    min_train_trajectory = []
    minJourneyId = 0
    min_i = 0

    knndtw = KnnDtw()
    #knndtw.fit(trainSet, 1)
    #knndtw.predict(testSetA1)
    #knndtw._dtw_distance(trainSet['Trajectory'][1], testSetA1[1])

    trainIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    start_time = time.time()
    curTime = start_time

    testNum = 0
    for trajectoryTest in testSetA1['Trajectory']:

        testNum += 1
        # if testNum <= 2:
        #     continue
        if testNum == 3:
            break

        array = []
        sorted_array = []

        print 'Checking for nearest-neighbor of test ' + testNum.__str__()

        # print trajectoryTest # DEBUG!

        for i in range(0, trainListSize):  # IDs and Trajectories are of the same size.

            # print trainIDs[i] # DEBUG!

            trajectoryTrain = trainTrajs[i]
            # print trajectoryTrain

            cost = knndtw._dtw_distance(trajectoryTest, trajectoryTrain)
            array.append((cost, i, trainIDs[i]))
            # print i.__str__() + ') Cost: ' + cost.__str__()
            if i == 0:
                min_cost = cost
                min_train_trajectory = trajectoryTrain
            elif cost < min_cost:
                min_cost = cost
                min_train_trajectory = trajectoryTrain
                min_i = i
                minJourneyId = trainIDs[min_i]
                print testNum.__str__() + '.' + min_i.__str__() + ') Found new minCost: ' + min_cost.__str__()

            if i == 500:
                break

            #print 'long: ' + trajectoryTest[1][1].__str__() + ' lat: ' + trajectoryTest[1][2].__str__()
            #print 'long: ' + trajectoryTrain[1][1].__str__() + ' lat: ' + trajectoryTrain[1][2].__str__()

        curTime = (time.time() - curTime) / 60

        sorted_array = sorted(array, key=lambda tup: tup[0])

        print '\nTest: ' + testNum.__str__() + ') finished in ' + curTime.__str__() + ' mins'\
              + '\nMin_journeyId: ' + minJourneyId.__str__() + ' min_i: ' + min_i.__str__()\
              + ' Min_long: ' + min_train_trajectory[1][1].__str__() + ' Min_lat: ' + min_train_trajectory[1][2].__str__() + ' Min_cost: ' + min_cost.__str__()\
              + '\nSorted mins: '

        for i in range(0, 5):
            print "TrajID: ", sorted_array[i][2], " , cost: ", sorted_array[i][0], " i: ", sorted_array[i][1]

        # Empty the arrays and plot the test-trajectory..
        timeStamps = []
        longtitutes = []
        latitudes = []

        timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(testSetA1['Trajectory'][1], timeStamps, longtitutes, latitudes)
        GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/task2A1/sample" + testNum.__str__() + "-test.html")

        for i in range(0, 5):
            curTrajectory = trainTrajs[sorted_array[i][1]]

            # Empty the arrays and plot the train-trajectory..
            timeStamps = []
            longtitutes = []
            latitudes = []

            timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(curTrajectory, timeStamps, longtitutes, latitudes)
            GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/task2A1/sample" + testNum.__str__() + "-train" + i.__str__() + ".html")

    print "Elapsed time of KNNwithDTW for 'test_set_a1': ", (time.time() - start_time) / 60, 'mins'


if __name__ == '__main__':
    findKearestNeighbors()
