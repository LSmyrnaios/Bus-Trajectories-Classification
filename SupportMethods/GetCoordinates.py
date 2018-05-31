

def getCoordinates(trajectory):

    longtitutes = []
    latitudes = []

    for triple in trajectory:
        #Avoid the triple[0] as it's the timestamp, which is not usable.
        longtitutes.append(triple[1])
        # print longtitutes
        latitudes.append(triple[2])
        # print latitudes

    return longtitutes, latitudes
