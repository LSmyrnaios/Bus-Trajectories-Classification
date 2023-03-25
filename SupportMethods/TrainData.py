from SupportMethods import readDatasets


def getListsOfTrainData(trainSet):
    journeyPatternIDs, trainTrajs = [], []

    for row in trainSet['journeyPatternId']:
        journeyPatternIDs.append(row)

    for row in trainSet['Trajectory']:
        trainTrajs.append(row)

    idListSize = journeyPatternIDs.__len__()
    if idListSize != trainTrajs.__len__():
        raise Exception("IDs and Trajectories had different sizes!")

    return journeyPatternIDs, trainTrajs, idListSize


if __name__ == '__main__':
    dataSets = readDatasets.read_dataset(True, True, False)
    trainSet = dataSets[0]
    testSetA1 = dataSets[1]

    getListsOfTrainData(trainSet)
    exit()
