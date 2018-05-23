import pandas as pd
from ast import literal_eval
from KNNwithDTW import KnnDtw
from SupportFuncs import GmPlot, GetTrajectorySets


def findKearestNeighbors():

    # Combine code and find nearest neighbors!

    trainSet = pd.read_csv('../Resources/DataSets/train_set.csv',
        converters={"Trajectory": literal_eval},
        index_col='tripId'
    )

    print "Finished loading train."

    testSetA1 = pd.read_csv( '../Resources/DataSets/test_set_a1.csv',
        converters={"Trajectory": literal_eval},
        sep="\t"
    )

    print "Finished loading test."

    i=0
    min_cost = 0
    min_sample = []
    min_i = 0

    knndtw = KnnDtw()
    #knndtw.fit(trainSet, 1)
    #knndtw.predict(testSetA1)
    #knndtw._dtw_distance(trainSet['Trajectory'][1], testSetA1[1])
    for row in trainSet['Trajectory']:

        # TODO - GET THE ID


        sample1 = row
        sample2 = testSetA1['Trajectory'][1]

        cost = knndtw._dtw_distance(sample1, sample2)
        print i.__str__() + ') Cost: ' + cost.__str__()
        if i==0:
            min_cost = cost
            min_sample = row
        elif(cost<min_cost):
            min_cost = cost
            min_sample = row
            min_i = i
        i += 1

        if(i==1500):break

        #print 'long: ' + sample1[1][1].__str__() + ' lat: ' + sample1[1][2].__str__()
        #print 'long: ' + sample2[1][1].__str__() + ' lat: ' + sample2[1][2].__str__()


    # print "Sample1: " + sample1.__str__()

    timeStamps = []
    longtitutes = []
    latitudes = []

    timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(trainSet['Trajectory'][min_i], timeStamps, longtitutes,
                                                                             latitudes)
    GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/sample1.html")

    # print "Sample2: " + sample2.__str__()

    timeStamps = []
    longtitutes = []
    latitudes = []

    timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(testSetA1['Trajectory'][1], timeStamps, longtitutes,
                                                                             latitudes)
    GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/sample2.html")

    print 'Min_long: ' + min_sample[1][1].__str__() + ' Min_lat: ' + min_sample[1][2].__str__() + ' min_cost: ' + min_cost.__str__() + ' min_i: ' + min_i.__str__()


if __name__ == '__main__':
    findKearestNeighbors()
