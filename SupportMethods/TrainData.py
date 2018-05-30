from SupportMethods import readDatasets

def getListsOfTrainData(trainSet):

    trainIDs, trainTrajs = [], []

    for row in trainSet['journeyPatternId']:
        trainIDs.append(row)

    for row in trainSet['Trajectory']:
        trainTrajs.append(row)

    idListSize = trainIDs.__len__()
    if idListSize != trainTrajs.__len__():
        raise Exception("IDs and Trajectories had different sizes!")

    return trainIDs, trainTrajs, idListSize


if __name__ == '__main__':

    dataSets = readDatasets.read_dataset(True, True, False)
    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    getListsOfTrainData(trainSet)
