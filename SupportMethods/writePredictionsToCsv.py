import os
import csv


def write_predictions_to_csv(test_data):
    # print predicted_data
    # print test_data

    dataSetsDir = "../../Resources/DataSets"
    if not os.path.isdir(dataSetsDir):
        os.makedirs(dataSetsDir)

    fileName = dataSetsDir + '/testSet_categories.csv'
    #with open(fileName, 'wb+') as csvfile:
    with open(fileName, mode='w+', encoding="utf8", newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(['Test_Trip_ID'] + ['Predicted_JourneyPatternID'])  # Write headers.
        for x in range(len(test_data)):
            csvWriter.writerow([test_data[x][0]] + [test_data[x][1]])  # Write id-pattern pairs.
