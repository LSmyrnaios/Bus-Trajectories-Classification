import os
import random
import time
from SupportMethods import GetCoordinates, readDatasets, TrainData, GmPlot


def data_visualization(K, dynamic_datasets_path):

    print("Going to visualize bus-trajectories..")
    dataSets = readDatasets.read_dataset(True, False, False, dynamic_datasets_path)
    trainSet = dataSets[0]

    #print trainSet.shape[0]  # DEBUG!
    #print trainSet['Trajectory']  # DEBUG!

    journeyPatternIDs, trainTrajs, trainListSize = TrainData.getListsOfTrainData(trainSet)

    storeMapsDir = os.path.join('..', '..', 'Resources', 'maps', 'task1')
    if not os.path.isdir(storeMapsDir):
        os.makedirs(storeMapsDir)

    selectedPatternIDs = []
    numOfSelectedPatterns = 0

    start_time = time.time()
    maxSecondsToWait = 120

    while True:
        if numOfSelectedPatterns == K:
            print('Finished plotting ' + K.__str__() + ' distinct random patterns.')
            break
        elif (time.time() - start_time) > maxSecondsToWait:
            print('The program could not find ' + K.__str__() + ' distinct random patterns in the specified time: ' + maxSecondsToWait.__str__())
            break

        randomTrain = random.randint(0, trainListSize-1)
        curPatternID = journeyPatternIDs[randomTrain]
        if curPatternID not in selectedPatternIDs:
            selectedPatternIDs.append(curPatternID)
            # plot the new pattern
            print('Going to plot a new random train..')
            longitudes, latitudes = GetCoordinates.getCoordinates(trainTrajs[randomTrain])
            fileName = "train" + randomTrain.__str__() + "_Pattern_" + curPatternID + ".html"
            GmPlot.gmPlot(latitudes, longitudes, os.path.join(storeMapsDir, fileName))
            numOfSelectedPatterns += 1


if __name__ == '__main__':
    K = 5
    dynamic_datasets_path = os.path.join('..', '..')
    data_visualization(K, dynamic_datasets_path)
    exit()
