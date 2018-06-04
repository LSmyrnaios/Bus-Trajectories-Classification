

class KMins:

    def __init__(self, K):
        self.K = K
        self.k_mins_arrayList = []
        self.max_cost_index = 0
        self.arrayListLength = 0


    def setMaxIndexOfArrayList(self):
        new_max_cost = 0
        for i in range(0, self.arrayListLength):
            if self.k_mins_arrayList[i][2] > new_max_cost:
                new_max_cost = self.k_mins_arrayList[i][2]
                self.max_cost_index = i


    def checkMaxCostAndInsert(self, new_triple):
        if self.arrayListLength < self.K:   # Fill the array
            self.k_mins_arrayList.append(new_triple)
            #print 'Filling the array with Cost: ' + self.k_mins_array[self.arrayLength][2].__str__()
            self.arrayListLength += 1
            if self.arrayListLength == self.K:  # When finished appending, set the max_index for later check.
                self.setMaxIndexOfArrayList()
        else:
            # If the given triple's cost is lessThan the array's max.. (that's the most common case)
            if new_triple[2] < self.k_mins_arrayList[self.max_cost_index][2]:
                # Replace max with given cost and find the new max (the "new_triple" it's uncertain if it's the new max).
                self.k_mins_arrayList[self.max_cost_index] = new_triple
                self.setMaxIndexOfArrayList()


    def getArrayList(self):
        return self.k_mins_arrayList


    def resetArrayList(self):
        del self.k_mins_arrayList[:]    # Delete the arrayList
        self.arrayListLength = 0    # Set length to zero. This is important, as we use this variable instead of taking the len() each time!
