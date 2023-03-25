import os
import time

from NearestNeighbors.K_arrayList.K_Maxs import KMaxs
from NearestNeighbors.task2A2.LCSS import lcs
from SupportMethods import readDatasets, TrainData, GetCoordinates, GmPlot


def runLCSS(K, dynamic_datasets_path):
    print('\nLCSS start..')

    dataSets = readDatasets.read_dataset(True, False, True, dynamic_datasets_path)

    trainSet = dataSets[0]
    testSetA2 = dataSets[1]

    journeyPatternIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    storeMapsDir = os.path.join('..', '..', 'Resources', 'maps', 'task2A2')
    if not os.path.isdir(storeMapsDir):
        os.makedirs(storeMapsDir)

    kMaxs = KMaxs(K)

    start_time = time.time()
    lastTime = start_time  # For in-the-middle elapsed-time.

    testNum = 0
    for trajectoryTest in testSetA2['Trajectory']:
        # print trajectoryTest

        testNum += 1

        # if testNum <= 2:
        #     continue
        # if testNum == 2:
        #     break

        nearestNeighbors = []
        sorted_subSeqsSizes = []

        print('\nChecking for ' + K.__str__() + ' longest common sub-sequences of test ' + testNum.__str__())

        # print trajectoryTest # DEBUG!
        iterations = 0
        sorted_subSequences = []

        for i in range(0, trainListSize):  # IDs and Trajectories are of the same size.
            # print i

            trajectoryTrain = trainTrajs[i]

            LongestCS = lcs(trajectoryTrain, trajectoryTest)

            if not LongestCS:
                continue
            # else:
            #     print i.__str__() + ') LCS length: ' + len(LongestCS).__str__()

            # if iterations == 10:
            #     break
            # else:
            #     iterations += 1

            kMaxs.checkMinLengthAndInsert([i, LongestCS, len(LongestCS)])

        curTime = time.time()
        curElapsedTime = curTime - lastTime
        lastTime = curTime

        print('\nTest: ' + testNum.__str__() + ') finished in ' + time.strftime("%H:%M:%S", time.gmtime(curElapsedTime)))

        # Plot test
        full_longitudes, full_latitudes = GetCoordinates.getCoordinates(trajectoryTest)
        fileName = "lcss" + testNum.__str__() + "-test-Time(sec)_" + curElapsedTime.__str__() + ".html"
        GmPlot.gmPlot(full_latitudes, full_longitudes, os.path.join(storeMapsDir, fileName), zoom=13)

        # So now we pic the top 5 and we plot them....
        sorted_subSequences = sorted(kMaxs.getArrayList(), reverse=True, key=lambda tup: tup[2])
        kMaxs.resetArrayList()  # Reset arrayList before going to the next testSet.

        for i in range(0, len(sorted_subSequences)):

            if i == K: break  # We only want the top K.

            print("Train " + sorted_subSequences[i][0].__str__() + ") PatternID: " \
                  + journeyPatternIDs[sorted_subSequences[i][0]].__str__() \
                  + ", MatchingPoints: " + sorted_subSequences[i][2].__str__() + ".html")

            curSubSeqTrajectory = trainTrajs[sorted_subSequences[i][0]]
            full_longitudes, full_latitudes = GetCoordinates.getCoordinates(curSubSeqTrajectory)

            curSubSeqTrajectory = sorted_subSequences[i][1]
            sub_longitudes, sub_latitudes = GetCoordinates.getCoordinates(curSubSeqTrajectory)
            fileName = "lcss" + testNum.__str__() + "-train" \
                       + sorted_subSequences[i][0].__str__() + "_PatternID_" \
                       + journeyPatternIDs[sorted_subSequences[i][0]].__str__() \
                       + "-MatchingPoints_" + sorted_subSequences[i][2].__str__() + ".html"
            GmPlot.gmPlotOfColours(full_latitudes, full_longitudes, sub_latitudes, sub_longitudes,
                                   os.path.join(storeMapsDir, fileName))

    print("\nElapsed time of KNNwithLCSS for 'test_set_a2': ",
          time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)), 'mins')


if __name__ == '__main__':
    K = 5
    dynamic_datasets_path = os.path.join('..', '..')
    runLCSS(K, dynamic_datasets_path)
    exit()
