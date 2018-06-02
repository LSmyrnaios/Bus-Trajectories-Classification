import random
from SupportMethods import GetCoordinates, readDatasets, TrainData
from DataVisualisation import GmPlot


def data_visualization():

    dataSets = readDatasets.read_dataset(True, False, False)
    trainSet = dataSets[0]

    #print trainSet.shape[0]  # DEBUG!
    #print trainSet['Trajectory']  # DEBUG!

    journeyPatternIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    selectedPatternIDs = []
    numOfSelectedPatterns = 0
    while True:

        if numOfSelectedPatterns == 5:
            break

        randomPattern = random.randint(0, trainListSize-1)
        curPatternID = journeyPatternIDs[randomPattern]
        if curPatternID not in selectedPatternIDs:
            selectedPatternIDs.append(curPatternID)
            # plot the new pattern
            longtitutes, latitudes = GetCoordinates.getCoordinates(trainTrajs[randomPattern])
            GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/task1/Pattern_" + curPatternID + ".html")
            numOfSelectedPatterns += 1


if __name__ == '__main__':
    data_visualization()
