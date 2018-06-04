import gmplot
import numpy as np


def gmPlot(latitudes, longtitutes, FullFilePath, zoom=12):

    gmap = gmplot.GoogleMapPlotter(np.mean(latitudes), np.mean(longtitutes), zoom)

    gmap.plot(latitudes, longtitutes, 'cornflowerblue', edge_width=10)

    gmap.draw(FullFilePath)


def gmPlotOfColours(fullLats, fullLongs, subLats, subLongs, FullFilePath, zoom=12):

    gmap = gmplot.GoogleMapPlotter(np.mean(fullLats), np.mean(fullLongs), zoom)

    gmap.plot(fullLats, fullLongs, 'green', edge_width=10)  # All green
    gmap.plot(subLats, subLongs, 'red', edge_width=10)  # Subsequence RED

    gmap.draw(FullFilePath)


