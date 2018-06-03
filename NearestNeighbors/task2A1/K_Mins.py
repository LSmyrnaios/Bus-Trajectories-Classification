

class KMins:

    def __init__(self, K):
        self.K = K
        self.k_mins_array = []
        self.max_cost_index = 0
        self.arrayLength = 0


    def checkMaxCostAndInsert(self, new_triple):

        if self.arrayLength < self.K:   # Fill the array
            self.k_mins_array.append(new_triple)
            self.arrayLength += 1
            return
        else:
            if new_triple[2] >= self.k_mins_array[self.max_cost_index][2]:    # If the given cost is greaterOrEqual to max.. (that's the most common case)
                return
            else:   # Replace max with given cost and find the new max.
                self.k_mins_array[self.max_cost_index] = new_triple
                new_max_cost = 0
                for i in range(0, self.arrayLength):
                    if self.k_mins_array[i][2] > new_max_cost:
                        new_max_cost = self.k_mins_array[i][2]
                        self.max_cost_index = i


    def getArray(self):
        return self.k_mins_array
