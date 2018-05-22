

def getTrajectorySets(row, timeStamps, longtitutes, latitudes):

    for trajectories in row:
        timeStamps.append(trajectories[0])
        # print timeStamps
        longtitutes.append(trajectories[1])
        # print longtitutes
        latitudes.append(trajectories[2])
        # print latitudes

    return timeStamps, longtitutes, latitudes