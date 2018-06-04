import pandas as pd
from ast import literal_eval


def read_dataset(shouldReadTrain, shouldReadTestA1, shouldReadTestA2):

    returnValues = []

    if shouldReadTrain:
        locationTrain = '../../Resources/DataSets/train_set.csv'
        trainSet = pd.read_csv(locationTrain,
            converters={"Trajectory": literal_eval},
            index_col='tripId'
        )
        print "Finished loading train: \'" + locationTrain + "\'"
        print 'TrainSet size: ' + trainSet.__len__().__str__()
        returnValues.append(trainSet)

    if shouldReadTestA1:
        locationTestA1 = '../../Resources/DataSets/test_set_a1.csv'
        testSetA1 = pd.read_csv(locationTestA1,
            converters={"Trajectory": literal_eval},
            sep="\t"
        )
        print "Finished loading testA1: \'" + locationTestA1 + "\'"
        print 'TestSetA1 size: ' + testSetA1.__len__().__str__()
        returnValues.append(testSetA1)

    if shouldReadTestA2:
        locationTestA2 = '../../Resources/DataSets/test_set_a2.csv'
        testSetA2 = pd.read_csv(locationTestA2,
            converters={"Trajectory": literal_eval},
            sep="\t"
        )
        print "Finished loading testA2: \'" + locationTestA2 + "\'"
        print 'TestSetA2 size: ' + testSetA2.__len__().__str__()
        returnValues.append(testSetA2)

    return returnValues
