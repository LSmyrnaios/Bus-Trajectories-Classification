import pandas as pd
from ast import literal_eval


def read_dataset(shouldReadTrain, shouldReadTestA1, shouldReadTestA2):

    returnValues = []

    if shouldReadTrain:
        trainSet = pd.read_csv('../Resources/DataSets/train_set.csv',
            converters={"Trajectory": literal_eval},
            index_col='tripId'
        )
        print "Finished loading train."
        print 'TrainSet size: ' + trainSet.__len__().__str__()
        returnValues.append(trainSet)

    if shouldReadTestA1:
        testSetA1 = pd.read_csv('../Resources/DataSets/test_set_a1.csv',
            converters={"Trajectory": literal_eval},
            sep="\t"
        )
        print "Finished loading testA1."
        print 'TestSetA1 size: ' + testSetA1.__len__().__str__()
        returnValues.append(testSetA1)

    if shouldReadTestA2:
        testSetA2 = pd.read_csv('../Resources/DataSets/test_set_a2.csv',
            converters={"Trajectory": literal_eval},
            sep="\t"
        )
        print "Finished loading testA2."
        print 'TestSetA2 size: ' + testSetA2.__len__().__str__()
        returnValues.append(testSetA2)

    return returnValues
