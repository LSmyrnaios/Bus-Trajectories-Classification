from SupportMethods import GmPlot, GetTrajectorySets, readDatasets


def data_visualization():

    dataSets = readDatasets.read_dataset(True, False, False)
    trainSet = dataSets[0]

    #print trainSet.shape[0]  # DEBUG!
    #print trainSet['Trajectory']

    trip_num = 0
    i = 0

    for row in trainSet['Trajectory']:
        #print trip_num, row

        if trip_num == 5:
            break

        timeStamps = []
        longtitutes = []
        latitudes = []

        if i % 11 == 1 or i % 17 == 1:
            timeStamps, longtitutes, latitudes = GetTrajectorySets.getTrajectorySets(row, timeStamps, longtitutes, latitudes)
            GmPlot.gmPlot(latitudes, longtitutes, "../Resources/maps/task1/TripMap" + i.__str__() + ".html")
            trip_num += 1

        i += 1


if __name__ == '__main__':
    data_visualization()
