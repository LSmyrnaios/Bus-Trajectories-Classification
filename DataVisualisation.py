import pandas as pd
from ast import literal_eval
from SupportFuncs import GmPlot, GetTrajectorySets


def data_visualization():

    trainSet = pd.read_csv(
        'Resources/DataSets/train_set.csv',
        converters={"Trajectory": literal_eval},
        index_col='tripId'
    )

    #print trainSet.shape[0]  # DEBUG!
    #print trainSet['Trajectory']

    trip_num = 0
    i=0

    for row in trainSet['Trajectory']:
        #print trip_num, row

        if ( trip_num == 5 ):
            break

        timeStamps = []
        longtitutes = []
        latitudes = []

        if ( i%7 == 1 ) :
            timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(row, timeStamps, longtitutes, latitudes)
            GmPlot.gmPlot(latitudes, longtitutes, "Resources/maps/TripMap" + i.__str__() + ".html")
            trip_num += 1

        i += 1


if __name__ == '__main__':
    data_visualization()
