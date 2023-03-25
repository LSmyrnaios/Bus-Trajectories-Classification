class KMaxs:

    def __init__(self, K):
        self.K = K
        self.k_maxs_arrayList = []
        self.min_length_index = 0
        self.arrayListLength = 0

    def setMinIndexOfArrayList(self):
        self.min_length_index = 0
        new_min_length = self.k_maxs_arrayList[self.min_length_index][2]
        for i in range(1, self.arrayListLength):
            if self.k_maxs_arrayList[i][2] < new_min_length:
                new_min_length = self.k_maxs_arrayList[i][2]
                self.min_length_index = i

    def checkMinLengthAndInsert(self, new_triple):
        if self.arrayListLength < self.K:   # Fill the array
            self.k_maxs_arrayList.append(new_triple)
            # print 'Filling the array with Cost: ' + self.k_mins_array[self.arrayLength][2].__str__()
            self.arrayListLength += 1
            if self.arrayListLength == self.K:  # When finished appending, set the max_index for later check.
                self.setMinIndexOfArrayList()
        else:
            # If the given triple's trajectory-length is greaterThan the array's min.. (that's the most common case)
            if new_triple[2] > self.k_maxs_arrayList[self.min_length_index][2]:
                # Replace current-min with given traj-length and find the new min (the "new_triple" it's uncertain if it's the new min itself).
                self.k_maxs_arrayList[self.min_length_index] = new_triple
                self.setMinIndexOfArrayList()

    def getArrayList(self):
        return self.k_maxs_arrayList

    def resetArrayList(self):
        del self.k_maxs_arrayList[:]  # Delete the arrayList
        self.arrayListLength = 0  # Set length to zero. This is important, as we use this variable instead of taking the len() each time!
