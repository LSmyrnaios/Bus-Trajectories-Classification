import gmplot
import pandas as pd
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
    for row in trainSet['Trajectory']:
        trip_num += 1
        #print trip_num, row

        for traj_set in row:
            print traj_set

            gmap = gmplot.GoogleMapPlotter(traj_set[0], traj_set[1], traj_set[2])

            # gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
            # gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
            # gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
            # #gmap.heatmap(heat_lats, heat_lngs)

            gmap.draw("Resources/maps/TripMap" + trip_num.__str__() + ".png")


if __name__ == '__main__':
    data_visualization()
