def getCoordinates(trajectory):
    longitudes = []
    latitudes = []

    for triple in trajectory:
        # Avoid the triple[0] as it's the timestamp, which is not usable.
        longitudes.append(triple[1])
        # print longitudes
        latitudes.append(triple[2])
        # print latitudes

    return longitudes, latitudes
