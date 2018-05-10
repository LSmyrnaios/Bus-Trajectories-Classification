import gmplot
import pandas as pd
import numpy as np
from ast import literal_eval


def data_visualization():

    trainSet = pd.read_csv(
        'Resources/train_set.csv',
        converters={"Trajectory": literal_eval},
        index_col='tripId'
    )

    #print trainSet.shape[0]  # DEBUG!
    #print trainSet['Trajectory']

    trip_num = 0
    i=0
    for row in trainSet['Trajectory']:
        #print trip_num, row

        if(trip_num==5):break

        timeStamps = []
        longtitutes = []
        latitudes = []
        if(i%7==1):
            for trajectories in row:
                timeStamps.append(trajectories[0])
                #print timeStamps
                longtitutes.append(trajectories[1])
                #print longtitutes
                latitudes.append(trajectories[2])
                #print latitudes

            gmap = gmplot.GoogleMapPlotter(np.mean(latitudes), np.mean(longtitutes), 12)

            gmap.plot(latitudes, longtitutes, 'cornflowerblue', edge_width=10)
            # gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
            # gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
            # gmap.heatmap(heat_lats, heat_lngs)

            gmap.draw("Resources/maps/TripMap" + i.__str__() + ".html")

            trip_num += 1
        i += 1


if __name__ == '__main__':
    data_visualization()
