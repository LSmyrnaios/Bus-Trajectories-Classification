

class KMins:

    def __init__(self, K):
        self.K = K
        self.k_mins_array = []
        self.max_cost_index = 0
        self.arrayLength = 0


    def setMaxIndexOfArray(self):
        new_max_cost = 0
        for i in range(0, self.arrayLength):
            if self.k_mins_array[i][2] > new_max_cost:
                new_max_cost = self.k_mins_array[i][2]
                self.max_cost_index = i


    def checkMaxCostAndInsert(self, new_triple):

        if self.arrayLength < self.K:   # Fill the array
            self.k_mins_array.append(new_triple)
            # print 'Filling the array with Cost: ' + self.k_mins_array[self.arrayLength][2].__str__()
            self.arrayLength += 1
            if self.arrayLength == self.K:  # When finished appending, set the max_index for later check.
                self.setMaxIndexOfArray()
        else:
            # If the given triple's cost is lessThan the array's max.. (that's the most common case)
            if new_triple[2] < self.k_mins_array[self.max_cost_index][2]:
                # Replace max with given cost and find the new max (the "new_triple" it's uncertain if it's the new max).
                self.k_mins_array[self.max_cost_index] = new_triple
                self.setMaxIndexOfArray()


    def getArray(self):
        return self.k_mins_array
