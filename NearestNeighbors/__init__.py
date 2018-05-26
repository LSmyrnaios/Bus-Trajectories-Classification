import time
from KNNwithDTW import KnnDtw
from SupportMethods import GmPlot, GetTrajectorySets, readDatasets


def findKearestNeighbors():

    # Combine code and find nearest neighbors!

    dataSets = readDatasets.read_dataset(True, True, False)

    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    start_time = time.time()

    i=0
    min_cost = 0
    min_sample = []
    minJourneyId = 0
    min_i = 0

    knndtw = KnnDtw()
    #knndtw.fit(trainSet, 1)
    #knndtw.predict(testSetA1)
    #knndtw._dtw_distance(trainSet['Trajectory'][1], testSetA1[1])

    testNum = 0
    for trajectoryTest in testSetA1['Trajectory']:

        testNum += 1
        # if testNum == 2:
        #     break

        print 'Checking for nearest-neighbor of test ' + testNum.__str__()

        # print trajectoryTest # DEBUG!

        trainIDs, trainTrajs = [], []

        for row in trainSet['journeyPatternId']:
            trainIDs.append(row)

        for row in trainSet['Trajectory']:
            trainTrajs.append(row)

        idListSize = trainIDs.__len__()
        if idListSize != trainTrajs.__len__():
            raise Exception("IDs and Trajectories had different sizes!")

        for i in range(0, idListSize):  # IDs and Trajectories are of the same size.

            # print trainIDs[i] # DEBUG!

            trajectoryTrain = trainTrajs[i]
            # print trajectoryTrain

            cost = knndtw._dtw_distance(trajectoryTest, trajectoryTrain)
            # print i.__str__() + ') Cost: ' + cost.__str__()
            if i == 0:
                min_cost = cost
                min_sample = trajectoryTrain
            elif cost < min_cost:
                min_cost = cost
                min_sample = trajectoryTrain
                minJourneyId = trainIDs[i]
                min_i = i

            # if i == 1500:
            #     break

            #print 'long: ' + trajectoryTest[1][1].__str__() + ' lat: ' + trajectoryTest[1][2].__str__()
            #print 'long: ' + trajectoryTrain[1][1].__str__() + ' lat: ' + trajectoryTrain[1][2].__str__()


        print 'Test: ' + testNum.__str__() + ') Min_journeyId: ' + minJourneyId.__str__() + ' min_i: ' + min_i.__str__()\
              + ' Min_long: ' + min_sample[1][1].__str__() + ' Min_lat: ' + min_sample[1][2].__str__() + ' Min_cost: ' + min_cost.__str__()

        timeStamps = []
        longtitutes = []
        latitudes = []

        timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(testSetA1['Trajectory'][1], timeStamps, longtitutes, latitudes)
        GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/task2A1/sample" + testNum.__str__() + "-test.html")

        # Empty the arrays and plot the train-trajectory..
        timeStamps = []
        longtitutes = []
        latitudes = []

        timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(trainSet['Trajectory'][min_i], timeStamps, longtitutes, latitudes)
        GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/task2A1/sample" + testNum.__str__() + "-train.html")

    print "Elapsed time of KNNwithDTW for 'test_set_a1': ", time.time() - start_time


if __name__ == '__main__':
    findKearestNeighbors()
