import gmplot
import numpy as np


# TODO - Maybe change to "Folium", based on OpenStreetMap, as GoogleMaps gives a low-quality-faded image with watermarks, if you don't pay for a key.
# https://python-visualization.github.io/folium/modules.html#module-folium.map
# https://www.openstreetmap.org/#map=3/37.37/7.37
# https://towardsdatascience.com/pythons-geocoding-convert-a-list-of-addresses-into-a-map-f522ef513fd6


def gmPlot(latitudes, longitudes, FullFilePath, zoom=12):
    gmap = gmplot.GoogleMapPlotter(np.mean(latitudes).__float__(), np.mean(longitudes).__float__(), zoom)

    gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)

    gmap.draw(FullFilePath)


def gmPlotOfColours(fullLats, fullLongs, subLats, subLongs, FullFilePath, zoom=12):
    gmap = gmplot.GoogleMapPlotter(np.mean(fullLats).__float__(), np.mean(fullLongs).__float__(), zoom)

    gmap.plot(fullLats, fullLongs, 'green', edge_width=10)  # All green
    gmap.plot(subLats, subLongs, 'red', edge_width=10)  # Subsequence RED

    gmap.draw(FullFilePath)
