from math import radians, cos, sin, asin, sqrt


# https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """

    # print "Calculating distance between (lon1, lat1)", lon1, lat1, " and (lon2, lat2)", lon2, lat2, "\n"

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = list(map(radians, [lon1, lat1, lon2, lat2]))

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    distance = c * r
    #print "Calculating distance between (lon1, lat1)", lon1, lat1, " and (lon2, lat2)", lon2, lat2, ". Distance: ", distance, "\n"
    # wait = input("PRESS ENTER TO CONTINUE.")
    return distance


if __name__ == '__main__':

    # Calculating distance between (lon1, lat1) -0.110302801597 0.930497960811  and (lon2, lat2) -0.112078447219 0.929978184306. Distance:  7.52834891357
    lon1 = -0.110302801597
    lat1 = 0.930497960811

    lon2 = -0.112078447219
    lat2 = 0.929978184306

    distance = haversine(lon1, lat1, lon2, lat2)

    print(("Distance: ", distance))