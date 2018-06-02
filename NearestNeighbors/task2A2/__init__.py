import os
import time
from NearestNeighbors.task2A2.LCSS import lcs
from SupportMethods import readDatasets, TrainData, GetCoordinates
from DataVisualisation import GmPlot


def runLCSS(K, useAllLCSs):
    print 'LCSS start..'

    dataSets = readDatasets.read_dataset(True, False, True)

    trainSet = dataSets[0]
    testSetA2 = dataSets[1]

    journeyPatternIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    storeMapsDir = "../../Resources/maps/task2A2"
    if not os.path.isdir(storeMapsDir):
        os.makedirs(storeMapsDir)

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

        print '\nChecking for ' + K.__str__() + ' most-common sub-sequences of test ' + testNum.__str__()

        # print trajectoryTest # DEBUG!
        iterations = 0
        subSequences = []
        sorted_subSequences =[]

        for i in range(0, trainListSize):  # IDs and Trajectories are of the same size.
            # print 'I am a happy little train...'
            # print i

            # if i <= 380 or (i >= 400 and i <= 500):
            #     continue

            trajectoryTrain = trainTrajs[i]

            if useAllLCSs:
                lists = lcs(trajectoryTrain, trajectoryTest, useAllLCSs)
                if len(lists) == 1:
                    if not lists[0]:
                        continue

                if iterations == 10:
                    break
                else:
                    iterations += 1

                # here we have all most common subs

                max_common_points = -1
                max_list = []

                for index in range(0, len(lists)):
                    if (len(lists[index]) > max_common_points):
                        max_common_points = len(lists[index])
                        max_list = lists[index]
                    print lists[index]

                if not max_list:
                    continue
                else:
                    print "Adding to the list!\n"
                    subSequences.append((i, max_list, max_common_points))

            else:
                LongestCS = lcs(trajectoryTrain, trajectoryTest, useAllLCSs)

                if not LongestCS:
                    continue
                # else:
                #     print LongestCS

                # if iterations == 10:
                #     break
                # else:
                #     iterations += 1

                #print "Adding to the list!\n"  # DEBUG!
                subSequences.append((i, LongestCS, len(LongestCS)))


        curTime = time.time()
        curElapsedTime = curTime - lastTime
        lastTime = curTime

        print '\nTest: ' + testNum.__str__() + ') finished in ' + time.strftime("%H:%M:%S", time.gmtime(curElapsedTime))

        # Plot test
        fullLongtitutes, fullLatitudes = GetCoordinates.getCoordinates(trajectoryTest)
        GmPlot.gmPlot(fullLatitudes, fullLongtitutes, storeMapsDir + "/lcss" + testNum.__str__() + "-test.html")

        # So now we pic the top 5 and we plot them....
        sorted_subSequences = sorted(subSequences, reverse=True, key=lambda tup: tup[2])
        sortedLength = len(sorted_subSequences)

        print "Sorted array length is ", sortedLength

        for i in range(0, sortedLength):
            if i == 5: break
            print sorted_subSequences[i]

            curSubSeqTrajectory = trainTrajs[sorted_subSequences[i][0]]
            fullLongtitutes, fullLatitudes = GetCoordinates.getCoordinates(curSubSeqTrajectory)

            curSubSeqTrajectory = sorted_subSequences[i][1]
            subLongtitutes, subLatitudes = GetCoordinates.getCoordinates(curSubSeqTrajectory)
            GmPlot.gmPlotOfColours(fullLatitudes, fullLongtitutes, subLatitudes, subLongtitutes,
                            storeMapsDir + "/lcss" + testNum.__str__() + "-train"
                            + sorted_subSequences[i][0].__str__() + "_PatternID_"
                            + journeyPatternIDs[sorted_subSequences[i][0]].__str__() + ".html")


    print "\nElapsed time of KNNwithLCSS for 'test_set_a2': ", time.strftime("%H:%M:%S", time.gmtime(
        time.time() - start_time)), 'mins'


if __name__ == '__main__':
    K = 5
    useAllLCSs = False
    runLCSS(K, useAllLCSs)
