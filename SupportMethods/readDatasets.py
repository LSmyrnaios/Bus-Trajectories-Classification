import os

import pandas as pd
from ast import literal_eval


def read_dataset(shouldReadTrain, shouldReadTestA1, shouldReadTestA2, dynamic_datasets_path=''):
    returnValues = []

    if shouldReadTrain:
        locationTrain = os.path.join(dynamic_datasets_path, 'Resources', 'DataSets', 'train_set.csv')
        print("Going to load training-set: \'" + locationTrain + "\'")
        trainSet = pd.read_csv(locationTrain,
                               converters={"Trajectory": literal_eval},
                               index_col='tripId')
        print("Finished loading training-set. Its size is: " + trainSet.__len__().__str__() + " records.")
        returnValues.append(trainSet)

    if shouldReadTestA1:
        locationTestA1 = os.path.join(dynamic_datasets_path, 'Resources', 'DataSets', 'test_set_a1.csv')
        print("Going to load testing-set: \'" + locationTestA1 + "\'")
        testSetA1 = pd.read_csv(locationTestA1,
                                converters={"Trajectory": literal_eval},
                                sep="\t")
        print("Finished loading testing-set. Its size is: " + testSetA1.__len__().__str__() + " records.")
        returnValues.append(testSetA1)

    if shouldReadTestA2:
        locationTestA2 = os.path.join(dynamic_datasets_path, 'Resources', 'DataSets', 'test_set_a2.csv')
        print("Going to load testing-set: \'" + locationTestA2 + "\'")
        testSetA2 = pd.read_csv(locationTestA2,
                                converters={"Trajectory": literal_eval},
                                sep="\t")
        print("Finished loading testing-set. Its size is: " + testSetA2.__len__().__str__() + " records.")
        returnValues.append(testSetA2)

    return returnValues
