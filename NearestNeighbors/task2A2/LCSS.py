from SupportMethods import readDatasets, HaversineDist

### solve the longest common subsequence problem

# get the matrix of LCS lengths at each sub-step of the recursive process
# (m+1 by n+1, where m=len(list1) & n=len(list2) ... it's one larger in each direction
# so we don't have to special-case the x-1 cases at the first elements of the iteration


def lcs_matrix(list1, list2):
    m = len(list1)
    n = len(list2)
    # construct the matrix, of all zeroes
    matrix = [[0] * (n+1) for row in range(m+1)]
    # populate the matrix, iteratively
    for row in range(1, m+1):
        for col in range(1, n+1):
            if((HaversineDist.haversine(list1[row - 1][1], list1[row - 1][2], list2[col - 1][1], list2[col - 1][2])) <= 0.2):
                #print "Here\n"
                #if list1[row - 1] == list2[col - 1]:
                # if it's the same element, it's one longer than the LCS of the truncated lists
                matrix[row][col] = matrix[row - 1][col - 1] + 1
            else:
                # they're not the same, so it's the the maximum of the lengths of the LCSs of the two options (different list truncated in each case)
                matrix[row][col] = max(matrix[row][col - 1], matrix[row - 1][col])
    # the matrix is complete
    return matrix


def longestCSS(matrix, list1, list2, index1, index2):

    if index1 == 0 or index2 == 0:
        return []
    if (HaversineDist.haversine(list1[index1 - 1][1], list1[index1 - 1][2], list2[index2 - 1][1], list2[index2 - 1][2])) <= 0.2:
        return longestCSS(matrix, list1, list2, index1-1, index2-1) + [list2[index2 -1]]
    if matrix[index1][index2 -1] > matrix[index1 -1][index2]:
        return longestCSS(matrix, list1, list2, index1, index2-1)

    return longestCSS(matrix, list1, list2, index1-1, index2)


# return a set of the sets of longest common subsequences in list1 and list2 or just a set containing the most-LCS
def lcs(list1, list2):

    # start the process...
    matrix = lcs_matrix(list1, list2)

    # len1 = len(list1)
    # len2 = len(list2)
    # if matrix[len1-1][len2-1] > 0:
    #     print "Common points: ", matrix[len1-1][len2-1]

    return longestCSS(matrix, list1, list2, len(list1), len(list2))


    # The following method test the LCSS. No use of KNN is made.
def runLCSStest():
    # get two lists
    # f = open("lists.txt")
    # contents = f.read().split("\n")
    # list1 = [int(i) for i in contents[0].split(",")]
    # list2 = [int(i) for i in contents[1].split(",")]

    dataSets = readDatasets.read_dataset(True, False, True)
    list1 = dataSets[0]
    list2 = dataSets[1]

    lists = lcs(list1, list2, True)

    # here we have all most common subs

    # so now we pic the top 5 and plot them....


    for l in lists:
        print(l)


if __name__ == "__main__":
    runLCSStest()
